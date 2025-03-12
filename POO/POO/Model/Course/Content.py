from abc import ABC, abstractmethod

class Content(ABC):
    """Classe abstrata para representar conteúdos de um curso."""
    
    def __init__(self, title):
        self._title = title

    @abstractmethod
    def list_content(self):
        pass

    def __str__(self):
        return self._title