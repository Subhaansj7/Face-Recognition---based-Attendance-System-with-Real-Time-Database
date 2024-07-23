import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("D:/Firebase/ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"---------------------------------------------"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name":"Subhaan Jirait",
            "major":"AI/ML",
            "Starting_year":2024,
            "total_attendance":6,
            "standing":"G",
             "year":1,
            "last_attendance_time":"2024-7-22 00:54:34"
        },
"852741":
        {
            "name":"Emily Blunt",
            "major":"Economics",
            "Starting_year":2023,
            "total_attendance":8,
            "standing":"B",
             "year":1,
            "last_attendance_time":"2024-7-22 00:54:34"
        },
"963852":
        {
            "name":"Elon Musk",
            "major":"Physics",
            "Starting_year":2023,
            "total_attendance":7,
            "standing":"G",
             "year":1,
            "last_attendance_time":"2024-7-22 00:54:34"
        }
}
for key,value in data.items():
    ref.child(key).set(value)
