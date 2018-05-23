# decorate-sort-undecorate

# sort in descending order
# by the sum of students' credits

students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]

print("student0:", students[0])


def decorate(student):
    # from student dict create a 2-tuple
    # (sum of credits, student)
    return sum(student['credits'].values()), student


def undecorate(decorated_student):
    # return original student dict
    return decorated_student[1]


students = sorted(map(decorate, students), reverse=True)
print(students)

students = list(map(undecorate, students))
print(students)

print("be carefull in case of equall sums!")
