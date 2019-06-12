courses = ['html', 'css', 'javascript', 'python',
           'javascript', 'react', 'react native', 'javascript']
print('Before', courses)

# for course in courses:
#     if courses.count(course) > 1:
#         courses.remove(course)
# print('After', courses)

courses.pop(-2)
print(courses)
