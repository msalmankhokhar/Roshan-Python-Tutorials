# List Comprehension

students = ['rohan', 'anushka', 'adil', 'ali']

# By using Loops
# new_list = []

# for x in students:
#     new_name = x + "_"
#     new_list.append(new_name)

# By using list comprehension
new_list = [ name + "_" for name in students ]
# print(new_list)

# dict comprehension

student_dict = { 
    'student_1' : 'salman',
    'student_2' : 'rohan',
    'student_3' : 'usman'
 }

# for key in student_dict:
#     student_dict[key] = student_dict[key] + "_"

new_dict = { key : student_dict[key] + "_" for key in student_dict }

print(new_dict)
    



