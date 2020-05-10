schema = {
    "Student": {
        "_id": "<objectId>",
        "first_name": "<string>",
        "last_name": "<string>",
    },
    "Assignment": {
        "_id": "<objectId>",
        "student_id": "<objectId>",
        "subject_id": "<objectId>",
        "grade": "<float>",
    },
    "Subject": {"_id": "<objectId>", "name": "<string>", "employee_id": "<objectId>",},
    "Classroom": {"_id": "<objectId>", "name": "<string>", "description": "<string>",},
    "Classes": {
        "_id": "<objectId>",
        "class_no": "<integer>",
        "date_time": "<datetime>",
        "classroom_id": "<objectId>",
        "subject_group_id": "<objectId>",
    },
    "Student_group": {"_id": "<objectId>", "subject_group_id": "<objectId>",},
    "Subject_group": {
        "_id": "<objectId>",
        "group_name": "<string>",
        "employee_id": "<objectId>",
        "subject_id": "<objectId>",
    },
    "Employee": {
        "_id": "<objectId>",
        "first_name": "<string>",
        "last_name": "<string>",
    },
}
