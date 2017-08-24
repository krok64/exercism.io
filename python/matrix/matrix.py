class Matrix():
    def __init__(self, matr_str):
        row = matr_str.split("\n")
        self.r_num = len(row)
        self.c_num = len(row[0].split())
        self.rows = []
        self.columns = []
        lst = []
        for r in row:
            cols = [int(x) for x in r.split()]
            self.rows.append(cols)
            lst.extend(cols)
        for i in range(self.c_num):
            self.columns.append(lst[i::self.c_num])

