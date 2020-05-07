from firebase import firebase







firebase_db_url = 'https://botlinex.firebaseio.com/'
firebase = firebase.FirebaseApplication(firebase_db_url,None)

''''
# Put data
freq_1 = {'frequency' : [108.3, 108.75]}
#freq_2  = {'frequency_2' : 108.75 , 'permit' : 'กรมสื่อสารทหารอากาศ'}
result = firebase.put('/user','1',freq_1)
'''

import json

data_vhf = {

    "freq_1": [91.25, "วิทยุชุมชนเมืองโคราช"],
    "freq_2": [96.25, "เมืองย่าเรดิโอ"],
    "freq_3": [99.40, "บลูสกายเรดิโอ,วิทยุชุมชนคนบ้านพระ"],



}

result = firebase.put('/user', '1', data_vhf)


def freq_datas(x):
    # user =  input(float("what freq do you want to find:   "))

    for i in result:
        data_freq = (result[i][0])  # return freqqq
        if float(x) == data_freq:
            return ((str(data_freq) + " MHz " +  result[i][1]))


print(freq_datas(99.40))









