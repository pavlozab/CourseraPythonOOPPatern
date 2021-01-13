# =============================================================================
# my solution
# =============================================================================

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
# coursera solution
# =============================================================================
# Объявим абстрактный декоратор
class AbstractEffect(Hero, ABC):

    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        return self.positive_effects

    @abstractmethod
    def get_negative_effects(self):
        return self.negative_effects

    @abstractmethod
    def get_stats(self):
        pass


# В AbstractPositive будем возвращать список наложенных отрицательных эффектов без изменений, чтобы не определять данный метод во всех положительных эффектах
class AbstractPositive(AbstractEffect):
    
    def get_negative_effects(self):
        return self.base.get_negative_effects()


# Объявим несколько положительных эффектов
class Berserk(AbstractPositive):
    
    def get_stats(self):
        # Получим характеристики базового объекта, модифицируем их и вернем
        stats = self.base.get_stats()
        stats["HP"] += 50
        stats["Strength"] += 7
        stats["Endurance"] += 7
        stats["Agility"] += 7
        stats["Luck"] += 7
        stats["Perception"] -= 3
        stats["Charisma"] -= 3
        stats["Intelligence"] -= 3
        return stats

    def get_positive_effects(self):
        # Модифицируем список эффектов, добавив в него новый эффект
        return self.base.get_positive_effects() + ["Berserk"]


class Blessing(AbstractPositive):
    
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 2
        stats["Endurance"] += 2
        stats["Agility"] += 2
        stats["Luck"] += 2
        stats["Perception"] += 2
        stats["Charisma"] += 2
        stats["Intelligence"] += 2
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Blessing"]


# Для отрицательных эффектов неизменным останется список положительных эффектов
class AbstractNegative(AbstractEffect):
    
    def get_positive_effects(self):
        return self.base.get_positive_effects()


# Аналогично положительным эффектам, объявим отрицательные
class Weakness(AbstractNegative):
    
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 4
        stats["Endurance"] -= 4
        stats["Agility"] -= 4
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Weakness"]


class Curse(AbstractNegative):
    
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 2
        stats["Endurance"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        stats["Perception"] -= 2
        stats["Charisma"] -= 2
        stats["Intelligence"] -= 2
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Curse"]


class EvilEye(AbstractNegative):
    
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Luck"] -= 10
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["EvilEye"]