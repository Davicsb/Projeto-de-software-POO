class QuizManager:
    def __init__(self, course_manager):
        self.course_manager = course_manager

    def add_quiz(self, course_title, question, answer):
        self.course_manager.add_quiz(course_title, question, answer)

    def remove_quiz(self, course_title, question):
        self.course_manager.remove_quiz(course_title, question)

    def view_quizzes(self, course_title):
        self.course_manager.view_quizzes(course_title)