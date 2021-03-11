#Homework 3 --- Course Grade Application
def askGrade():
    midterm = int(input("Vize notunuzu giriniz:"))
    project = int(input("Proje ödevi notunuzu giriniz:"))
    final = int(input("Final sınavı notunuzu giriniz:"))
    grade = int(midterm*0.3 + project*0.3 + final*0.4)
    return grade

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

allGrades = [student1["grade"],student2["grade"],student3["grade"],student4["grade"],student5["grade"]]

allGrades.sort(reverse=True)

print(allGrades)
