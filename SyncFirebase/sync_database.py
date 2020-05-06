from firebase import firebase







firebase_db_url = 'https://botlinex.firebaseio.com/'
firebase = firebase.FirebaseApplication(firebase_db_url,None)


# Put data
freq_1 = {'frequency' : [108.3, 108.75]}
#freq_2  = {'frequency_2' : 108.75 , 'permit' : 'กรมสื่อสารทหารอากาศ'}
result = firebase.put('/user','1',freq_1)











