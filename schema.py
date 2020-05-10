import pymongo

schema = [
    {
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
        "Subject": {
            "_id": "<objectId>",
            "name": "<string>",
            "employee_id": "<objectId>",
        },
        "Classroom": {
            "_id": "<objectId>",
            "name": "<string>",
            "description": "<string>",
        },
        "Classes": {
            "_id": "<objectId>",
            "class_no": "<integer>",
            "date_time": "<datetime>",
            "classroom_id": "<objectId>",
            "subject_group_id": "<objectId>",
        },
        "Student_group": {"_id": "<objectId>", "subject_group_id": "<objectId>"},
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
        "_version": "1",
        "_indices": [],
    },
    {
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
        "MainSubject": {
            "_id": "<objectId>",
            "name": "<string>",
            "employee_id": "<objectId>",
            "subject_info_id": "<objectId>",
        },
        "Subject": {
            "_id": "<objectId>",
            "name": "<string>",
            "employee_id": "<objectId>",
            "subject_info_id": "<objectId>",
        },
        "SubjectInfo": {
            "_id": "<objectId>",
            "subject_id": "<objectId>",
            "ects": "<integer>",
            "hours": "<integer>",
            "description": "<integer>",
        },
        "Classroom": {
            "_id": "<objectId>",
            "name": "<string>",
            "capabilities": [
                {
                    "subject_id": "<objectId>",
                    "computer_no": "<integer>",
                    "projector": "<bool>",
                    "description": "<string>",
                }
            ],
        },
        "Classes": {
            "_id": "<objectId>",
            "class_no": "<integer>",
            "date_time": "<datetime>",
            "classroom_id": "<objectId>",
            "subject_group_id": "<objectId>",
        },
        "Student_group": {"_id": "<objectId>", "subject_group_id": "<objectId>"},
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
        "_version": "2",
        "_indices": [
            {
                "Classroom": [
                    ("capabilites.subject_id", pymongo.ASCENDING),
                    ("capabilites.computer_no", pymongo.ASCENDING),
                ]
            },
            {
                "Classroom": [
                    ("capabilites.subject_id", pymongo.ASCENDING),
                    ("capabilites.projector", pymongo.ASCENDING),
                ]
            },
        ],
    },
    {
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
        "MainSubject": {
            "_id": "<objectId>",
            "name": "<string>",
            "employee_id": "<objectId>",
            "subject_info_id": "<objectId>",
            "field_id": "<objectId>",
        },
        "Subject": {
            "_id": "<objectId>",
            "name": "<string>",
            "employee_id": "<objectId>",
            "subject_info_id": "<objectId>",
            "field_id": "<objectId>",
        },
        "SubjectInfo": {
            "_id": "<objectId>",
            "subject_id": "<objectId>",
            "ects": "<integer>",
            "hours": "<integer>",
            "description": "<integer>",
        },
        "Field": {
            "_id": "<objectId>",
            "name": "<string>",
            "disciplines": ["<string>"],
        },
        "Classroom": {
            "_id": "<objectId>",
            "name": "<string>",
            "descriptions": [{"class_id": "<objectId>", "description": "<string>"}],
        },
        "Classes": {
            "_id": "<objectId>",
            "class_no": "<integer>",
            "date_time": "<datetime>",
            "classroom_id": "<objectId>",
            "subject_group_id": "<objectId>",
        },
        "Student_group": {"_id": "<objectId>", "subject_group_id": "<objectId>"},
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
        "_version": "3",
        "_indices": [{"Classroom": ("descriptions.description")}],
    },
]
