from Model.Course.Content import Content

class Lesson(Content):
    """Representa uma aula com título e URL."""
    
    def __init__(self, title, url):
        super().__init__(title)
        self._url = url

    def list_content(self):
        return f"Lesson: {self._title} - URL: {self._url}"