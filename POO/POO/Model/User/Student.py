from Model.User.User import User

class Student(User):
    def __init__(self, username, password, age, course, paid, progress=0):
        super().__init__(username, password)
        self._age = age
        self._course = course
        self._paid = paid
        self._progress = progress

    def get_role(self):
        return "Student"
    
    def setProgress(self, progress):
        self._progress = progress
        
    def getProgress(self):
        if self._progress == 100:
            return "Completed"
        elif self._progress == 0:
            return "Not started"
        return self._progress
    
    def __str__(self):
        return (f"Student(ID: {self._id}, Username: {self._username}, Password: {self.password}, Age: {self._age}, "
                f"Course: {self._course}, Paid: {self._paid}, Progress: {self._progress}%)")