import smtplib
import xlrd
import pyrebase
import wolframalpha
import wikipedia
import pyttsx3
import requests
import time

config = {
    'apiKey': "API KEY", # API KEY Here
    'authDomain': "name of app domain",
    'databaseURL': "url ",
    'projectId': "id details",
    'storageBucket': "storage bucked",
    'messagingSenderId': "sener id"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()
temp=""

def base():
    global temp
    users = db.child('fir-test-e5d24').child('custo').child("-M0SenkdvhvicCboKSfm").get()
    h = users.val()

    result = h['pno']
    if result == '1':
        users = db.child('fir-test-e5d24').child('custo').child("-M0SenkdvhvicCboKSfm").update({'pno': 0})
        temp= h['name']
        print(temp)
    else:
        base()

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
        
def speak(ans):
    users = db.child('fir-test-e5d24').child('custo').child("-M0SenkbFLOOLa6v9S-5").update({'pno': 1,'name':'"'+ans+'\""'})
def sendmail():
    global temp
    time.sleep(1)
    speak('say message')
    base()
    msg=temp
    speak('say email')
    base()
    mid = temp

    print(mid,msg)
    import mail
    mail.send(mid,msg)
    time.sleep(1)
    speak('email sent')
    cmod()      
def sms():
    speak('Say Phone Number')
    users = db.child('fir-test-e5d24').child('custo').child("-M0SenkdvhvicCboKSfm").get()
    h = users.val()
    result = h['pno']
    if result == '1':
        users = db.child('fir-test-e5d24').child('custo').child("-M0SenkdvhvicCboKSfm").update({'pno': 0})
        no = h['name']
        print(no)
    else:
        sms()
    time.sleep(1)
    speak('Say message')
    global temp
    base()
    msg=temp

    url = "https://www.fast2sms.com/dev/bulk"
    no = no.replace('"', '')

    payload = "sender_id=FSTSMS&message=" + str(msg) + "&language=english&route=p&numbers=" + str(no)

    print(payload)

    headers = {
        'authorization': "wZQGLgmX9hPUNMxSHxzQhGhktYZgo21lLeGoPnWE5zL6PkkP4Y9Fd4Z2m06X",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    speak('sms sent')
    cmod()
def rdata():
    global temp
    base()
    pp=temp.replace('"',"")

    
    loc = ("data.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for i in range(1, 212):
        g = sheet.cell_value(i, 0)
        if int(pp) == g:
            pp = str(pp)
            pp.replace("L", "")
            index = i
            break
    idno = int(sheet.cell_value(i, 0))
    name = str(sheet.cell_value(i, 1))
    pno = str(sheet.cell_value(i, 2))
    msgg = "Name :" + name + "Id :" + str(idno) + "\nPhone Number: " + str(pno)
    speak(msgg)
    cmod()    
def cmds(g):
    if 'sms' in g:
        sms()
    elif 'email' in g:
        sendmail()
    elif 'roll' in g:
        rdata()
    elif 'home' in g:
        gett()
    else:
        speak('No command found')
        cmod()
        
        
def cmod():
    speak('command mode activated')
    users = db.child('fir-test-e5d24').child('custo').child("-M0SenkdvhvicCboKSfm").get()
    h = users.val()

    result = h['pno']
    if result == '1':
        users = db.child('fir-test-e5d24').child('custo').child("-M0SenkdvhvicCboKSfm").update({'pno': 0})
        print(h['name'])
        cmds(str(h['name']))

    else:
        cmod()


def info(query):
    print(query)
    query = query.lower()
    print(query)
    try:

        if 'tom' in query:
            query = query.replace('tom', '')
            client = wolframalpha.Client("API KEY")
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
gett()
