# Remove duplicate elements from list

courses = ['html', 'css', 'javascript', 'python',
           'javascript', 'react', 'react native', 'javascript']
print('Before', courses)

for course in courses:
    if courses.count(course) > 1:
        courses.remove(course)
print('After', courses)
