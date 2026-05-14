class Student:
    name: str
    major: str
    gpa: int
    is_on_probation: bool

    # what student attribute should have
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def studentclassification(self):
        if self.gpa >= 7.5:
            return "Good"
        else:
            return "Not Good"
