import pyrebase

config = {
  'apiKey': "AIzaSyCU4lzswP8--5mQkFklgLrFLUl-sVekkAM",
  'authDomain': "dynamicqr-3c23d.firebaseapp.com",
  'projectId': "dynamicqr-3c23d",
  'storageBucket': "dynamicqr-3c23d.appspot.com",
  'messagingSenderId': "236258808030",
  'appId': "1:236258808030:web:7649a57dcf8cb87a79b24f",
  'measurementId': "G-K5NQB928E1",
  'databaseURL': 'https://dynamicqr-3c23d-default-rtdb.asia-southeast1.firebasedatabase.app/'
}

firebase = pyrebase.initialize_app(config)