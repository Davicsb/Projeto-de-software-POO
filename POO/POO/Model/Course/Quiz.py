from Model.Course.Content import Content

class Quiz(Content):
    """Representa um questionário com pergunta e resposta."""
    
    def __init__(self, title, question, answer):
        super().__init__(title)
        self._question = question
        self._answer = answer

    def list_content(self):
        return f"Quiz: {self._title}\nQuestion: {self._question}\nAnswer: {self._answer}"
