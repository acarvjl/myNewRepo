import random

# creating a list of students to create groups of two!
stuGroup = ["Kevin Alcocer", "Vanessa Barajas", "Donald Cao", "Adrian Carvajal", "Mark Edmunds", \
           "Luren Fahey", "Nathan Gibson", "Juli Gregson", "Matthew Gutierrez", "Sierra McCullough", \
           "Gilbert Negrillo", "Taylor Nii", "Jay Parangalan", "Richard Sanchez", "Kimberly Schank", \
           "Eslam Shousha", "Karnvir Singh", "Conor Smith", "Thai Thao"]

# creating variable to hold groups
random_group = []

# go through the list to create groups of two each and randomize them and create groups
group_size = 2
while len(stuGroup) >= group_size:
    group_random = random.sample(stuGroup, group_size)
    random_group.append(group_random)

    for stu in group_random:
        stuGroup.remove(stu)


if len(stuGroup) > 0:
    random_group.append(stuGroup)

for i, group in enumerate(random_group):
    print(f"Group {i + 1}: {group}")
