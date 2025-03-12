from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def view(self):
        pass