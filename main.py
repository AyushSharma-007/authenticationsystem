pip install pyrebase4
import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "assignment-efe1b-default-rtdb.firebaseapp.com",
  "databaseURL": "https://assignment-efe1b-default-rtdb.firebaseio.com/",
  "storageBucket": "assignment-efe1b-default-rtdb.appspot.com"
}

firebase = pyrebase.initialize_app(config)
