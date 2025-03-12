class LessonManager:
    def __init__(self, course_manager):
        self.course_manager = course_manager

    def add_class(self, course_title, class_title, url):
        self.course_manager.add_class(course_title, class_title, url)

    def remove_class(self, course_title, class_title):
        self.course_manager.remove_class(course_title, class_title)

    def view_classes(self, course_title):
        self.course_manager.view_classes(course_title)