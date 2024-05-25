grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a_gr = sum(grades[0])/len(grades[0])
b_gr = sum(grades[1])/len(grades[1])
j_gr = sum(grades[2])/len(grades[2])
k_gr = sum(grades[3])/len(grades[3])
s_gr = sum(grades[4])/len(grades[4])
all_gr = a_gr, b_gr, j_gr, k_gr, s_gr
all_stud = sorted(students)
tuple(all_stud)
all_dict = dict(zip(all_stud, all_gr))
print(all_dict)



