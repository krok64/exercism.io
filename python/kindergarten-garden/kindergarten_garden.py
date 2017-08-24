plant_names = {"R":"Radishes", "G":"Grass", "C": "Clover", "V": "Violets"}
default_stud_list = ["Alice", "Bob", "Charlie", "David",
  "Eve", "Fred", "Ginny", "Harriet",
  "Ileana", "Joseph", "Kincaid", "Larry"]

class Garden(object):
    def __init__(self, rows, students=default_stud_list):
        self.row1, self.row2 = rows.split("\n")
        self.students = sorted(students)

    def plants(self, stud_name):
        stud_pozition = self.students.index(stud_name)
        ret_list = []
        ret_list.append(plant_names[self.row1[stud_pozition*2]])
        ret_list.append(plant_names[self.row1[stud_pozition*2+1]])
        ret_list.append(plant_names[self.row2[stud_pozition*2]])
        ret_list.append(plant_names[self.row2[stud_pozition*2+1]])
        return ret_list
