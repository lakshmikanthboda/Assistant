import smtplib
import xlrd
import pyrebase
import wolframalpha
import wikipedia
import pyttsx3
import requests
import time

config = {
    'apiKey': "AIzaSyBOrWtvqsaEPfYjNhPUV9YvEQ_t6aV4iug",
    'authDomain': "fir-test-e5d24.firebaseapp.com",
    'databaseURL': "https://fir-test-e5d24.firebaseio.com",
    'projectId': "fir-test-e5d24",
    'storageBucket': "fir-test-e5d24.appspot.com",
    'messagingSenderId': "332768780595"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

def gett():
    users = db.child('fir-test-e5d24').child('custo').child("-M0SenkdvhvicCboKSfm").get()
    h = users.val()

    result = h['pno']
    if result == '1':
        users = db.child('fir-test-e5d24').child('custo').child("-M0SenkdvhvicCboKSfm").update({'pno': 0})
        if 'cmd' in h['name']:
            cmod()
        else:
            info(h['name'])
    else:
        gett()
        




def info(query):
    print(query)
    query = query.lower()
    print(query)
    try:

        if 'tom' in query:
            query = query.replace('tom', '')
            client = wolframalpha.Client("PX76HL-QL5KJTK9UW")
            res = client.query(query)
            ans = next(res.results).text
            ans = ans.replace('Stephen Wolfram', 'Tech Breed')
            ans = ans.replace('Wolfram|Alpha', 'Tachyon')
            ans = ans.replace('18/05/2009', '25-02-2020')
            print(ans)
            speak(ans)
            gett()

    except Exception:
        try:
            query = query.replace('tom', '')
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
            gett()

        except:
            speak("It is weird but I got nothing ")
            gett()
    gett()
