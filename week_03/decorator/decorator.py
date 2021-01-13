# =============================================================================
# Скрипт для тестирования решений студентов по заданию "Создание декоратора
# класса" (тесты содержат примеры, приведенные в описании задания)
# https://stepik.org/lesson/106937/step/4?unit=81460
# Скопируйте код вашего решения в секцию ВАШ КОД и запустите скрипт
# =============================================================================
from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points, 
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость 
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


# =============================================================================
# начало секции ВАШ КОД
# =============================================================================
# Поместите в этой секции реализацию классов AbstractEffect, AbstractPositive,
# AbstractNegative, Berserk, Blessing, Curse, EvilEye, Weakness из вашего
# решения

from abc import ABC, abstractmethod

class AbstractEffect(Hero, ABC): 
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_stats(self):
        pass

class AbstractPositive(AbstractEffect, ABC):
    @abstractmethod
    def get_positive_effects(self):
        pass

    def get_negative_effects(self):
        return self.base.get_negative_effects()
    
    def get_stats(self):
        return self.base.get_stats()

class AbstractNegative(AbstractEffect, ABC):
    @abstractmethod
    def get_negative_effects(self):
        pass

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_stats(self):
        return self.base.get_stats()

class Berserk(AbstractPositive):
    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        positive_effects.append(str(type(self).__name__))
        return positive_effects.copy()
    
    def get_stats(self):
        stats = self.base.get_stats()
        for i in ('Strength', 'Endurance', 'Agility', 'Luck'):
            stats[i] += 7
        for i in ('Perception', 'Charisma', 'Intelligence'):
            stats[i] -= 3
        stats['HP'] += 50
        return stats.copy() 

class Blessing(AbstractPositive):
    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        positive_effects.append(str(type(self).__name__))
        return positive_effects.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        for i in ("Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"):
            stats[i] += 2
        return stats.copy()

class Weakness(AbstractNegative):
    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append(str(type(self).__name__))
        return negative_effects.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        for i in ('Strength', 'Endurance', 'Agility'):
            stats[i] -= 4
        return stats.copy()

class Curse(AbstractNegative):
    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append(str(type(self).__name__))
        return negative_effects.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        for i in ("Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"):
            stats[i] -= 2
        return stats.copy()

class EvilEye(AbstractNegative):
    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append(str(type(self).__name__))
        return negative_effects.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Luck'] -= 10
        return stats.copy()



# =============================================================================
# конец секции ВАШ КОД
# =============================================================================

if __name__ == '__main__':
    # создадим героя
    hero = Hero()
    # проверим правильность характеристик по-умолчанию
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    # проверим список отрицательных эффектов
    assert hero.get_negative_effects() == []
    # проверим список положительных эффектов
    assert hero.get_positive_effects() == []
    # наложим эффект Berserk
    brs1 = Berserk(hero)
    # проверим правильность изменения характеристик
    assert brs1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 22,
                                'Perception': 1,
                                'Endurance': 15,
                                'Charisma': -1,
                                'Intelligence': 0,
                                'Agility': 15,
                                'Luck': 8}
    # проверим неизменность списка отрицательных эффектов
    assert brs1.get_negative_effects() == []
    # проверим, что в список положительных эффектов был добавлен Berserk
    assert brs1.get_positive_effects() == ['Berserk']
    # повторное наложение эффекта Berserk
    brs2 = Berserk(brs1)
    # наложение эффекта Curse
    cur1 = Curse(brs2)
    # проверим правильность изменения характеристик
    assert cur1.get_stats() == {'HP': 228,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 27,
                                'Perception': -4,
                                'Endurance': 20,
                                'Charisma': -6,
                                'Intelligence': -5,
                                'Agility': 20,
                                'Luck': 13}
    # проверим правильность добавления эффектов в список положительных эффектов
    assert cur1.get_positive_effects() == ['Berserk', 'Berserk']
    # проверим правильность добавления эффектов в список отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # снятие эффекта Berserk
    cur1.base = brs1
    # проверим правильность изменения характеристик
    assert cur1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 20,
                                'Perception': -1,
                                'Endurance': 13,
                                'Charisma': -3,
                                'Intelligence': -2,
                                'Agility': 13,
                                'Luck': 6}
    # проверим правильность удаления эффектов из списка положительных эффектов
    assert cur1.get_positive_effects() == ['Berserk']
    # проверим правильность эффектов в списке отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # проверим незменность характеристик у объекта hero
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    print('All tests - OK!')



