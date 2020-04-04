schema = {
    "Student": {
        "student_id": "<objectId>",
        "first_name": "<string>",
        "last_name": "<string>",
    },
    "Assignment": {
        "assignment_id": "<objectId>",
        "student_id": "<objectId>",
        "subject_id": "<objectId>",
        "grade": "<float>",
    },
    "Subject": {
        "subject_id": "<objectId>",
        "name": "<string>",
        "employee_id": "<objectId>",
    },
    "Classroom": {
        "classroom_id": "<objectId>",
        "name": "<string>",
        "description": "<string>",
    },
    "Classes": {
        "classes_id": "<objectId>",
        "class_no": "<integer>",
        "date_time": "<datetime>",
        "classroom_id": "<objectId>",
        "group_subject_id": "<objectId>",
    },
    "Student_group": {
        "student_id": "<objectId>",
        "group_subject_id": "<objectId>",
    },
    "Subject_group": {
        "group_subject_id": "<objectId>",
        "group_name": "<string>",
        "employee_id": "<objectId>",
        "subject_id": "<objectId>",
    },
    "Employee": {
        "employee_id": "<objectId>",
        "first_name": "<string>",
        "last_name": "<string>",
    }
}
