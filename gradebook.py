last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

# Create a list of subjects and grades
# This will help us organize our gradebook
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

#Manually create a two-dimensional combining subjects and grades
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

#Print the manually created gradebook
print(gradebook) 

#Add "computer science" and "visual arts" to the gradebook
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

#Change the grade for visual arts to 98
gradebook[5][1] = 98

#Remote the grade 85 from poetry and add "Pass"
gradebook[2].remove(85)
gradebook[2].append("Pass")

#Combine the two gradebooks
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)