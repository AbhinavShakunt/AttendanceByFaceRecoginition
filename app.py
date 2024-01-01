from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendance3sem-default-rtdb.firebaseio.com/"
})

# Set up route for displaying attendance
@app.route('/')
def display_attendance():
    # Get the student ID for which you want to calculate the total attendance
    student_id = '321654'  # Replace with the desired student ID

    # Get a reference to the student
    student_ref = db.reference('Students').child(student_id)

    # Get the total attendance count for the student
    total_attendance = student_ref.child('total_attendance').get()

    # Get the attendance count for each month
    attendance_by_month = student_ref.child('attendance_by_month').get()

    return render_template('attendance.html', student_id=student_id, total_attendance=total_attendance, attendance_by_month=attendance_by_month)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
