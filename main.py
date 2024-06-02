pip install pyrebase4
import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "assignment-efe1b-default-rtdb.firebaseapp.com",
  "databaseURL": "https://assignment-efe1b-default-rtdb.firebaseio.com/",
  "storageBucket": "assignment-efe1b-default-rtdb.appspot.com"
}
db = firebase.database()
db.child("users").child("Morty")
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)
firebase = pyrebase.initialize_app(config)
// used to insert the database in it 
