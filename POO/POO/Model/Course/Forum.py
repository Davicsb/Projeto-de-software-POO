from Model.Course.Content import Content

class Forum(Content):
    """Representa um fórum de discussão com comentários."""
    
    def __init__(self, title, name, comment):
        super().__init__(title)
        self._name = name
        self._comment = comment

    def list_content(self):
        return f"Forum: {self._title} - {self._name}: {self._comment}"
