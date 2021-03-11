#Homework 3 --- Course Grade Application

#Asking to students grade and return grade with grade formula
def askGrade():
    midterm = int(input("Vize notunuzu giriniz:"))
    project = int(input("Proje ödevi notunuzu giriniz:"))
    final = int(input("Final sınavı notunuzu giriniz:"))
    grade = int(midterm*0.3 + project*0.3 + final*0.4)
    return grade

#5 Student dictionaries "grade" key is return from askGrade function
student1 = {
    "name": "Ahmet",
    "grade": askGrade()
}

student2 = {
    "name": "Mehmet",
    "grade": askGrade()
}

student3 = {
    "name": "Ali",
    "grade": askGrade()
}
student4 = {
    "name": "Veli",
    "grade": askGrade()
}
student5 = {
    "name": "Ayşe",
    "grade": askGrade()
}

#Indexing all students in allGrades list
allGrades = [student1["grade"],student2["grade"],student3["grade"],student4["grade"],student5["grade"]]

#Sorted the list, reverse sort for highest grade come first
allGrades.sort(reverse=True)
