#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


# =======================================================================================
# Клас вектор
# =======================================================================================
class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        """возвращает разность двух векторов"""
        return Vec2d(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        """возвращает сумму двух векторов"""
        return Vec2d(self.x + other.x, self.y + other.y)

    def __len__(self):
        """возвращает длину вектора"""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        return Vec2d(self.x * k, self.y * k)

    def int_pair(self):
        """ возвращает кортеж из двух целых чисел (текущие координаты вектора) """
        return int(self.x), int(self.y)

# =======================================================================================
# Класс замкнутых ломаных Polyline
# =======================================================================================
class Polyline:
    def __init__(self, points=None, speeds=None):
        self.points = points
        self.speeds = speeds

    def set_points(self):
        """ функция перерасчета координат опорных точек """
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p] = Vec2d(- self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def draw_points(self, width=3, color=(255, 255, 255)):
        """ функция отрисовки точек на экране """
        for p in self.points:
            pygame.draw.circle(gameDisplay, color,
                                (int(p.x), int(p.y)), width)
    
    @staticmethod
    def draw_line(points, width=3, color=(255, 255, 255)):
        """ функция отрисовки линий на экране """
        for p_n in range(-1, len(points) - 1):
            pygame.draw.line(gameDisplay, color,
                            (int(points[p_n].x), int(points[p_n].y)),
                            (int(points[p_n + 1].x), int(points[p_n + 1].y)), width)

    @staticmethod
    def draw_help():
        """функция отрисовки экрана справки программы"""
        gameDisplay.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["Num+", "More points"])
        data.append(["Num-", "Less points"])
        data.append(["", ""])
        data.append([str(steps), "Current points"])

        pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            gameDisplay.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            gameDisplay.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))
        
# =======================================================================================
# Класс Knot
# =======================================================================================
class Knot(Polyline):
    def __init__(self, points, speeds):
        super().__init__(points, speeds)

    def __get_point(self, base_points,  alpha, deg=None):
        """ функция возвращающая точку """
        if deg is None:
            deg = len(base_points) - 1
        if deg == 0:
            return base_points[0]
        return (base_points[deg] * alpha) + (self.__get_point(base_points, alpha, deg - 1) * (1 - alpha))

    def __get_points(self, base_points, count):
        """ функция возвращающая точки """
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.__get_point(base_points, i * alpha))
        return res

    def get_knot(self, count):
        """ функция ... """
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)
            res.extend(self.__get_points(ptn, count))
        return res

    def draw_line(self, steps, width=3, color=(255, 255, 255)):
        Polyline.draw_line(self.get_knot(steps), width, color)
        

# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    points = Knot(points=[], speeds=[])
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = Knot(points=[], speeds=[])
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                points.points.append(Vec2d(event.pos[0], event.pos[1]))
                points.speeds.append(Vec2d(random.random() * 2, random.random() * 2))


        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        points.draw_points()
        points.draw_line(steps, 3, color)

        if not pause:
            points.set_points()
        if show_help:
            Polyline.draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
