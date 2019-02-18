from collections import namedtuple


class School(object):
    def __init__(self):

        SchoolRoster = namedtuple("SchoolRoster", "name grade")
        SchoolRoster_List = []
        self.SchoolRoster = SchoolRoster
        self.SchoolRoster_List = SchoolRoster_List

    def add_student(self, name, grade):

        new_student = self.SchoolRoster(name=name, grade=grade)
        self.SchoolRoster_List.append(new_student)

    def roster(self):

        return [
            name
            for name, grade in sorted(
                self.SchoolRoster_List, key=lambda x: (x.grade, x.name)
            )
        ]

    def grade(self, grade_number):

        return [
            name
            for name, grade in sorted(self.SchoolRoster_List, key=lambda x: x.name)
            if grade == grade_number
        ]
