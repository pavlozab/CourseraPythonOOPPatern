
#   {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}


from abc import ABC, abstractmethod


class ObservableEngine(Engine): # Engine
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)
        
    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message) 


class AbstractObserver(ABC):
    @abstractmethod
    def update(sel, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()  # зберігаємо title

    def update(self, message):
        self.achievements.add(message['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()  # зберігаємо весь словарь

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)