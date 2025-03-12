from Model.Course import Lesson, Quiz, Forum

class Course:
    """Representa um curso com aulas, quizzes e fórum."""
    
    def __init__(self, title, hours, teacher, paid):
        self._title = title
        self._hours = hours
        self._teacher = teacher
        self._paid = paid
        self._lessons = []
        self._quizzes = []
        self._forums = []

    @property
    def title(self):
        return self._title

    @property
    def hours(self):
        return self._hours

    @property
    def teacher(self):
        return self._teacher

    @property
    def paid(self):
        return self._paid

    def add_lesson(self, lesson):
        self._lessons.append(lesson)

    def add_quiz(self, quiz):
        self._quizzes.append(quiz)

    def add_forum(self, forum):
        self._forums.append(forum)

    def __str__(self):
        lesson_titles = ', '.join(str(lesson) for lesson in self._lessons[:2]) if self._lessons else "No lessons"
        quiz_titles = ', '.join(str(quiz) for quiz in self._quizzes[:2]) if self._quizzes else "No quizzes"
        forum_titles = ', '.join(str(forum) for forum in self._forums[:2]) if self._forums else "No forums"

        return (f"Course(title: {self._title}, hours: {self._hours}, teacher: {self._teacher}, paid: {self._paid}, "
                f"lessons: [{lesson_titles}], quizzes: [{quiz_titles}], forums: [{forum_titles}])")