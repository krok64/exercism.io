class School(object):
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add(self, name, grade):
        self.students[name] = grade

    def grade(self, n):
        return [x for x in self.students if self.students[x]==n]

    def sort(self):
        ret_list=[]
        for grade in set(sorted(self.students.values())):
            stud_list=[]
            for stud in self.students:
                if self.students[stud] == grade:
                    stud_list.append(stud)
            g_list=(grade, tuple(sorted(stud_list)))
            ret_list.append(g_list)
        return ret_list




