import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendance3sem-default-rtdb.firebaseio.com/"
})

# Get the student ID for which you want to calculate the total attendance
student_id = '321654'  # Replace with the desired student ID

# Get a reference to the student
student_ref = db.reference('Students').child(student_id)

# Get the total attendance count for the student
total_attendance = student_ref.child('total_attendance').get()

# Check if total_attendance is not None
if total_attendance is not None:
    print("Total Attendance for Student", student_id, ":", total_attendance)
else:
    print("Total Attendance for Student", student_id, "not found.")

# Get the monthly attendance data
monthly_attendance = student_ref.child('attendance_by_month').get()

# Check if monthly_attendance is not None
if monthly_attendance is not None:
    # Iterate over the months and print the attendance count
    for month, attendance in monthly_attendance.items():
        print("Attendance for Student", student_id, "in Month", month, ":", attendance)
else:
    print("No monthly attendance data available for Student", student_id)
