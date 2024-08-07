registrations = (
    {"student_id": 1, "class_id": 5},
    {"student_id": 1, "class_id": 6},
    {"student_id": 1, "class_id": 10},
    {"student_id": 1, "class_id": 15},
    {"student_id": 1, "class_id": 20},
    {"student_id": 2, "class_id": 5},
    {"student_id": 2, "class_id": 10},
    {"student_id": 2, "class_id": 15},
    {"student_id": 2, "class_id": 20},
    {"student_id": 3, "class_id": 5},
    {"student_id": 3, "class_id": 10},
    {"student_id": 3, "class_id": 15},
    {"student_id": 3, "class_id": 20},
    {"student_id": 6, "class_id": 4},
    {"student_id": 6, "class_id": 9},
    {"student_id": 6, "class_id": 14},
    {"student_id": 6, "class_id": 19},
    {"student_id": 7, "class_id": 5},
    {"student_id": 7, "class_id": 10},
    {"student_id": 7, "class_id": 15},
    {"student_id": 7, "class_id": 20},
    {"student_id": 9, "class_id": 5},
    {"student_id": 9, "class_id": 10},
    {"student_id": 9, "class_id": 15},
    {"student_id": 9, "class_id": 20},
    {"student_id": 11, "class_id": 4},
    {"student_id": 11, "class_id": 9},
    {"student_id": 11, "class_id": 14},
    {"student_id": 11, "class_id": 19},
    {"student_id": 12, "class_id": 5},
    {"student_id": 12, "class_id": 10},
    {"student_id": 12, "class_id": 15},
    {"student_id": 12, "class_id": 20},
)


fkey = [
    f"{registration['student_id']}&{registration['class_id']}"
    for registration in registrations
]

print(fkey)
