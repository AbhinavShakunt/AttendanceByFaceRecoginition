import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendance3sem-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654": {
        "name": "Abhinav Shakunt",
        "major": "MCA",
        "starting_year": 2022,
        "total_attendance": 33,
        "standing": "B",
        "year": 2,
        "last_attendance_time": "2023-06-23 17:48:34",
        "attendance_by_month": {
            "06": 33
        }
    },
    "852741": {
        "name": "Emly Blunt",
        "major": "Economics",
        "starting_year": 2021,
        "total_attendance": 12,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34",
        "attendance_by_month": {
            "06": 12
        }
    },
    "963852": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34",
        "attendance_by_month": {
            "06": 7
        }
    }
}

for key, value in data.items():
    ref.child(key).set(value)

print("Data added to the database.")
