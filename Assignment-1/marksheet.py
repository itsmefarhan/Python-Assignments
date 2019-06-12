
name = input('Enter Your Name: ')
roll_number = input('Enter Your Roll Number: ')
institute = input('Enter Your Institute Name: ')

subject_1 = int(input('Enter marks obtained in Physics '))
subject_2 = int(input('Enter marks obtained in Chemistry '))
subject_3 = int(input('Enter marks obtained in Maths '))
subject_4 = int(input('Enter marks obtained in English '))
subject_5 = int(input('Enter marks obtained in Computer Science '))

print('\n\t\t***********************************************************************************')
print('\t\t*\t\t\t\t\tMARKSHEET\t\t\t\t  *')
print('\t\t***********************************************************************************')

print("\n\t\t\tStudent's Name: \t" + name)
print("\t\t\tRoll #: \t\t" + roll_number)
print('\t\t\tInstitute: \t\t' + institute)

print('\t\t___________________________________________________________________________________')
print('\n\t\t\tSubject \t\tMarks')
print('\t\t___________________________________________________________________________________')
print('\n\t\t\tPhysics \t\t' + str(subject_1))
print('\t\t\tChemistry \t\t' + str(subject_2))
print('\t\t\tMaths \t\t\t' + str(subject_3))
print('\t\t\tEnglish \t\t' + str(subject_4))
print('\t\t\tComputer Science \t' + str(subject_5))

sum = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
print('\t\t\t\t\t      ------')
print('\t\t\tMarks Obtained \t\t' + str(sum))
print('\t\t\t\t\t      ------')
percentage = (sum / 500) * 100

if percentage >= 80:
    print('\n\t\t\tGrade: \t\tA+')
    print('\t\t\tPercentage: \t' + str(percentage) + '%')
elif percentage >= 70:
    print('\n\t\t\tGrade: \t\tA')
    print('\t\t\tPercentage: \t' + str(percentage) + '%')
elif percentage >= 60:
    print('\n\t\t\tGrade: \t\tB')
    print('\t\t\tPercentage: \t' + str(percentage) + '%')
elif percentage >= 50:
    print('\n\t\t\tGrade: \t\tC')
    print('\t\t\tPercentage: \t' + str(percentage) + '%')
else:
    print('\n\t\t\tGrade: \t\tFailed')
    print('\t\t\tPercentage: \t' + str(percentage) + '%')

print('\n\t\t***********************************************************************************')