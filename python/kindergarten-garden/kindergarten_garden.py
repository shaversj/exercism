from collections import defaultdict


class Garden(object):
    def __init__(
        self,
        diagram,
        students=[
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ],
    ):
        self.diagram = diagram.split("\n")
        self.plant_map = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}
        sorted_students = sorted(students)

        sill = 1
        student_to_sill_map = defaultdict(list)
        for name in sorted_students:
            student_to_sill_map[name].append(sill)
            student_to_sill_map[name].append(sill + 1)
            sill += 2

        self.student_to_sill_map = student_to_sill_map

    def plants(self, name):
        """Returns a list of plants that were planted by the student"""
        student_plants = []
        for row in self.diagram:
            for cup_number, plant in enumerate(row, 1):
                student_window_sill = self.student_to_sill_map[name]
                if cup_number in student_window_sill:
                    student_plants.append(self.plant_map[plant])

        return student_plants
