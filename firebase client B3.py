import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("firebase-creds.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project.firebaseio.com'
})

def get_sensor_data():
    ref = db.reference('/sensors')
    return ref.get()