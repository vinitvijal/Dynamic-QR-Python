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

storage = firebase.storage()
auth = firebase.auth()

user = auth.sign_in_with_email_and_password('vinitvijal@gmail.com', 'password')
token = user['localId']
# print(user)

def upload_doc():
    file = eval(input('Your File : '))
    abc = file[-15:]
    storage.child("doc/"+abc).put(file)
    file_link = storage.child("doc/"+abc, ).get_url(token)
    print(file_link)

upload_doc()      


# abc = ''
# # as admin
# storage.child("images/%s"abc).put("%s"abc)
# # as user
# storage.child("images/example.jpg").put("example2.jpg", user['idToken'])