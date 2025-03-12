import os
import time
from Model import Course, Lesson, Quiz, Forum

def clear_terminal():
    """Limpa o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

class CourseManager:
    def __init__(self):
        self.courses = {}

    def add_course(self, title, teacher, hours, ispaid):
        if title in self.courses:
            print("This course is already registered!")
        else:
            self.courses[title] = Course(title, hours, teacher, ispaid)
            print(f"Course '{title}' added successfully!")
        time.sleep(2)

    def delete_course(self, title):
        if title in self.courses:
            del self.courses[title]
            print(f"Course '{title}' deleted successfully!")
        else:
            print("Course not found!")
        time.sleep(2)

    def update_course(self, old_title, new_title=None, new_hours=None, new_teacher=None):
        if old_title in self.courses:
            course = self.courses[old_title]
            if new_title:
                self.courses[new_title] = self.courses.pop(old_title)
                course._title = new_title
            if new_hours:
                course._hours = new_hours
            if new_teacher:
                course._teacher = new_teacher
            print(f"'{old_title}' has been updated successfully!")
        else:
            print("Course not found!")
        time.sleep(2)

    def add_class(self, course_title, class_title, url):
        if course_title in self.courses:
            lesson = Lesson(class_title, url)
            print(lesson._title, lesson._url)
            self.courses[course_title].add_lesson(lesson)
            print(f"Class '{class_title}' added to course '{course_title}'")
        else:
            print("Course not found!")
        time.sleep(2)

    def view_classes(self, course_title):
        if course_title in self.courses:
            course = self.courses[course_title]
            if not course._lessons:
                print("No classes found!")
            else:
                print(f"Classes in {course.title}:")
                for lesson in course._lessons:
                    print(lesson.list_content())
        else:
            print("Course not found!")
        time.sleep(2)

    def remove_class(self, course_title, class_title):
        if course_title in self.courses:
            course = self.courses[course_title]
            course._lessons = [lesson for lesson in course._lessons if lesson.title != class_title]
            print(f"Class '{class_title}' removed successfully!")
        else:
            print("Course not found!")
        time.sleep(2)

    def add_quiz(self, course_title, question, answer):
        if course_title in self.courses:
            quiz = Quiz(course_title, question, answer)
            self.courses[course_title]._quizzes.append(quiz)
            print(f"Quiz added to course '{course_title}'")
        else:
            print("Course not found!")
        time.sleep(2)

    def view_quizzes(self, course_title):
        if course_title in self.courses:
            course = self.courses[course_title]
            if not course._quizzes:
                print("This Course hasn’t quizzes found!")
            else:
                print(f"Quizzes in {course._title}:")
                for quiz in course._quizzes:
                    print(quiz.list_content())
        else:
            print("Course not found!")
        time.sleep(2)

    def remove_quiz(self, course_title, question):
        if course_title in self.courses:
            course = self.courses[course_title]
            course._quizzes = [quiz for quiz in course._quizzes if quiz._question != question]
            print(f"Quiz '{question}' removed successfully!")
        else:
            print("Course not found!")
        time.sleep(2)

    def list_courses(self, student_paid_condition, teacher=None):
        if not self.courses:
            print("No courses available!")
        elif student_paid_condition == True:
            for course in self.courses.values():
                if teacher:
                    if course.teacher == teacher:
                        print(f"Title: {course.title}, Teacher: {course.teacher}, Hours: {course.hours}")
                else:
                    print(f"Title: {course.title}, Teacher: {course.teacher}, Hours: {course.hours}")
        else:
            for course in self.courses.values():
                if course.paid == False:
                    print(f"Title: {course.title}, Teacher: {course.teacher}, Hours: {course.hours}")
        time.sleep(2)

    def add_comment_in_forum(self, course_title, name, comment):
        if course_title in self.courses:
            new_comment = Forum(course_title, name, comment)
            self.courses[course_title]._forums.append(new_comment)
            print(f"Comment added to forum of '{course_title}'")
        else:
            print("Course not found!")
        time.sleep(2)

    def view_comments_in_forum(self, course_title):
        if course_title in self.courses:
            course = self.courses[course_title]
            if not course._forums:
                print("No comments found!")
            else:
                print(f"Forum in {course.title}:")
                for comment in course._forums:
                    print(comment.list_content())
        else:
            print("Course not found!")
        time.sleep(2)

    def remove_comment(self, course_title, name, comment):
        clear_terminal()
        if course_title in self.courses:
            course = self.courses[course_title]
            course._forums = [c for c in course._forums if c._name != name or c._comment != comment]
            print(f"Comment from '{name}' removed successfully!")
        else:
            print("Course not found!")
        time.sleep(2)