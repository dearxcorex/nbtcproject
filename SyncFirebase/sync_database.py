from firebase import firebase

firebase_db_url = 'https://botlinex.firebaseio.com/'
firebase = firebase.FirebaseApplication(firebase_db_url,None)


# Put data
freq_1 = {'frequency' : [108.3, 108.75]}
#freq_2  = {'frequency_2' : 108.75 , 'permit' : 'กรมสื่อสารทหารอากาศ'}

result = firebase.put('/user','1',freq_1)





#get data
def air_frq():
    get_result = firebase.get('/user', '1')
    datas = []
    for i in get_result['frequency']:
        datas.append(i)
    for k in datas:
        if k == 108.3:
            print("กรมสื่อสารทหารอากาศ")

