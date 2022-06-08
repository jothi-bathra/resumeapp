#Importing required Libraries
#flask for API development
from flask import Flask, request, render_template, redirect, session, url_for
import pymongo
import bcrypt
#creating instance for Flask 
app=Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CV"]
mycol = mydb["register"]
mycol2=mydb["skills"]
mycol3=mydb["feedback"]



#getting input from frontend
@app.route('/register',methods=['GET','POST'])
def register():
    message='Register here'
    if "email" in session:
        return redirect(url_for("logged_in"))
    details=request.form
    name= details['name']
    email= details['email']
    passw = details['pass']
    email_found = mycol.find_one({"email": email})
    if email_found:
        message = 'This email already exists in database'
        return render_template('register.html', message=message)
    else:
        mydict = { "name": name, "email": email, "pass": passw }

        x = mycol.insert_one(mydict)
    

        return render_template('login.html')

#@app.route('/logged_in')
#def logged_in():
 #   if "email" in session:
  #      email = session["email"]
   
   #     return render_template('logged_in.html', email=email)
    #else:
     #   return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'
    #if "email" in session:
     #   return redirect(url_for("logged_in"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        #check if email exists in database
        email_found = mycol.find_one({"email": email})
        if email_found:
            
            email_val = email_found['email']
            passwordcheck = email_found['pass']
            #encode the password and check if it matches
            if (password==passwordcheck):
      #          session["email"] = email_val
                return render_template('main.html')
            else:
                
           # if "email" in session:
            #    return redirect(url_for("logged_in"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)


#@app.route("/logout", methods=["POST", "GET"])
#def logout():
 #   if "email" in session:
  #      session.pop("email", None)
   #     return render_template("signout.html")
    #else:
     #   return render_template('home.html')


@app.route("/alogin", methods=["POST", "GET"])
def alogin():
    message = 'Please login to your account'
    if request.method == "POST":
        uname = request.form.get("uname")
        password = request.form.get("password")
        if uname=='admin':
            if (password=='admin1234'):
                return render_template('ahome.html')
            else:
                message = 'Wrong password'
                return render_template('adminlogin.html', message=message)
        else:
            message = 'Username is incorrect'
            return render_template('adminlogin.html', message=message)
    return render_template('adminlogin.html', message=message)


@app.route('/feedback',methods=['GET','POST'])
def feedback():
    print("0")
    #if "email" in session:
     #   return redirect(url_for("logged_in"))
    details=request.form
    name= details['name']
    email= details['email']
    feedback = details['feedback']
    print("1")

    mydict = { "name": name, "email": email, "feedback": feedback }
    print("2")

    x = mycol3.insert_one(mydict)


    return render_template('home.html')

@app.route('/radd',methods=['GET','POST'])
def radd():
    message='Job/Skill'
    
    details=request.form
    role= details['role']
    skill= details['skill']

    role_found = mycol2.find_one({"role": role},{"skill":skill})

    if role_found:
        message = 'This job and skill already exists in database'
        return render_template('addr.html', message=message)
    else:
        mydict = { "role": role, "skill": skill }

        x = mycol2.insert_one(mydict)
    

        return render_template('ahome.html')

@app.route("/aview")
def aview():
    customer = (mycol.find())
    return render_template('aview.html', customer=customer)

@app.route('/feed')
def feed():
    return render_template('feedback.html')

@app.route('/slist')
def slist():
    return render_template('skill.html')



@app.route('/viewr')
def viewr():
    skills = (mycol2.find())
    return render_template('viewr.html', skills=skills)
    


@app.route('/addr')
def addr():
    return render_template('addr.html')


@app.route('/updater')
def updater():
    return render_template('updater.html')

@app.route('/homepage')
def homapage():
    return render_template('home.html')

@app.route('/registerpage')
def registerpage():
    return render_template('register.html')

@app.route('/loginpage')
def loginpage():
    return render_template('login.html')

@app.route('/adminloginpage')
def adminloginpage():
    return render_template('adminlogin.html')

@app.route('/inputpage')
def inputpage():
    return render_template('input.html')

@app.route('/')
def submit():
    return render_template('home.html')



@app.route('/input',methods=['GET','POST'])
def input():
    msg=''
    detail=[]
    details=request.form
    
    name=details['name']
    detail.append(name)
    email=details['email']
    detail.append(email)
    phone=details['phone']
    detail.append(phone)
    linked=details['linkedin']
    detail.append(linked)
    about=details['about']
    detail.append(about)
    s1=details['s1']
    detail.append(s1)
    s2=details['s2']
    detail.append(s2)
    s3=details['s3']
    detail.append(s3)
    s4=details['s4']
    detail.append(s4)
    a1=details['a1']
    detail.append(a1)
    a2=details['a2']
    detail.append(a2)
    a3=details['a3']
    detail.append(a3)
    a4=details['a4']
    detail.append(a4)
    p1=details['p1']
    detail.append(p1)
    pd1=details['pd1']
    detail.append(pd1)
    p2=details['p2']
    detail.append(p2)
    pd2=details['pd2']
    detail.append(pd2)
    univ=details['univ']
    detail.append(univ)
    degree=details['degree']
    detail.append(degree)
    cgpa=details['cgpa']
    detail.append(cgpa)
    school=details['school']
    detail.append(school)
    mark=details['12mark']
    detail.append(mark)

    mydict2 = { "degree": degree, "skill1": s1, "skill4": s4, "skill3": s3, "skill2": s2  }

    x = mycol2.insert_one(mydict2)
    
    
    return render_template('resume.html', detail=detail)




if __name__ == '__main__':
    app.run(debug=True)
