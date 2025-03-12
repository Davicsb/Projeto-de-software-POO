class ForumManager:
    def __init__(self, course_manager):
        self.course_manager = course_manager

    def add_comment(self, course_title, name, comment):
        self.course_manager.add_comment_in_forum(course_title, name, comment)

    def remove_comment(self, course_title, name, comment):
        self.course_manager.remove_comment(course_title, name, comment)

    def view_comments(self, course_title):
        self.course_manager.view_comments_in_forum(course_title)