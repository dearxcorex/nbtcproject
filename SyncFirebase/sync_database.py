from firebase import firebase

firebase_db_url = 'https://botlinex.firebaseio.com/'
firebase = firebase.FirebaseApplication(firebase_db_url,None)


# Put data
freq_1 = {'frequency' : '108.3' , 'permit' : 'กรมสื่อสารทหารอากาศ'}
#freq_2  = {'frequency_2' : '108.75' , 'permit' : 'กรมสื่อสารทหารอากาศ'}

result = firebase.put('/user','1',freq_1)
#result2 = firebase.put('/user','2',freq_2)

#print("Engineer 1", result)
#print("Engineer 2", result2)







#get data

get_result = firebase.get('/user','1' )
print (get_result['permit'])