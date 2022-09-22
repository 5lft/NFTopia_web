from django.shortcuts import render,redirect

#email = "test@test.com"
#user = auth.get_user_by_email(email)
#print('Successfully fetched user data: {0}'.format(user.uid))

import pyrebase
 
# For Firebase JS SDK v7.20.0 and later, measurementId is optional
config={
    "apiKey": "AIzaSyAegckHxdAju4f5MLVOZ-JWg_giW8Lxtu8",
    "authDomain": "nftopiadb.firebaseapp.com",
    "databaseURL": "https://nftopiadb-default-rtdb.firebaseio.com",
    "projectId": "nftopiadb",
    "storageBucket": "nftopiadb.appspot.com",
    "messagingSenderId": "688142264061",
    "appId": "1:688142264061:web:566e65ff22db1005530094",
    "measurementId": "G-WK6DXH0GBP"
}

# Initialising database,auth and firebase for further use
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def login(request):
    
    return render(request,"login.html")

def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"login.html",{"message":message})
    session_id=user['idToken']

    request.session['uid']=str(session_id)
    request.session['email'] = email


    return redirect('gallery')
 
def logout(request):
    try:
        del request.session['uid']
        del request.session['email']
    except:
        pass
    return redirect('gallery')