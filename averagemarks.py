marksInPython = float(input("Enter marks in Python:"))
marksInJava = float(input("Enter marks in Java: "))
marksInPhP = float(input("Enter marks in PhP: "))
marksInJavaScript = float(input("Enter marks in JavaScript: "))
no_of_sub=4
if marksInPython<0:
    print("Marks cannot be negative")
    marksInPython = - marksInPython
if marksInJava<0:
    print("Marks cannot be negative")
    marksInJava = - marksInJava
if marksInJavaScript<0:
    print("Marks cannot be negative")
    marksInJavaScript = - marksInJavaScript
if marksInPhP<0:
    print("Marks cannot be negative")
    marksInPhP = - marksInPhP

print(f"""Python: {marksInPython}
Java: {marksInJava}
PhP: {marksInPhP}
JavaScript: {marksInJavaScript}""")
if marksInJava>=40 and marksInJava<=50:
    grade="D"
elif marksInJava>=90 and marksInJava<=100:
    grade = "A"
elif marksInJava>=80 and marksInJava<=90:
    grade= "B"
else:
    grade = "Fail"

print(grade)
total = marksInJavaScript+marksInJava+marksInPhP+marksInPython
average = total/no_of_sub
percentage=(total/400)*100
print(f"""
Total Marks:{total}
Average: {average}
Percentage: {percentage}%""")