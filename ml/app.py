from flask import Flask,render_template,request,url_for
import joblib
import numpy as np

app = Flask(__name__)


def setLevelValues(value):
    

    if value == 'junior':
        return 0
    elif value == 'middle':
        return 1
    else:
        return 2

def setExperienceValues(value):
    

    if value == '0 - 1 Yıl':
        return 0
    elif value == '1 - 3 Yıl':
        return 1
    elif value == '3 - 5 Yıl':
        return 2
    elif value == '5 - 7 Yıl':
        return 3
    elif value == '7 - 10 Yıl':
        return 4
    elif value == '10 - 14 Yıl':
        return 5
    else :
        return 6

    

def setPositionValues(value):
    if value =="cto" :
        return 1,0,0,0,0,0,0,0,0,0,0,0,0,0
    elif value=="dataScience":
        return 0,1,0,0,0,0,0,0,0,0,0,0,0,0
    elif value == "dba":
        return 0,0,1,0,0,0,0,0,0,0,0,0,0,0
    elif value == "devopsEng":
        return 0,0,0,1,0,0,0,0,0,0,0,0,0,0
    elif value == "embeddedDev":
        return 0,0,0,0,1,0,0,0,0,0,0,0,0,0
    elif value=="frontend":
        return 0,0,0,0,0,1,0,0,0,0,0,0,0,0
    elif value=='fullStack':
        return 0,0,0,0,0,0,1,0,0,0,0,0,0,0
    elif value=="gameDev":
        return 0,0,0,0,0,0,0,1,0,0,0,0,0,0
    elif value=="mobileApp":
        return 1,0,0,0,0,0,0,0,1,0,0,0,0,0
    elif value=="others":
        return 0,0,0,0,0,0,0,0,0,1,0,0,0,0
    elif value=="qaTest":
        return 0,0,0,0,0,0,0,0,0,0,1,0,0,0
    elif value=="softwareArch":
        return 1,0,0,0,0,0,0,0,0,0,0,1,0,0
  
    elif value=="softwareManager":
        return 0,0,0,0,0,0,0,0,0,0,0,0,1,0
    elif value=="teamLead":
        return 0,0,0,0,0,0,0,0,0,0,0,0,0,1
    else:
        return 0,0,0,0,0,0,0,0,0,0,0,0,0,0

def setCompanyType(value):
    if value=="reklam":
        return 1,0,0,0,0,0,0,0
    elif value=="eticaret":
        return 0,1,0,0,0,0,0,0
    elif value=="finans":
        return 0,0,1,0,0,0,0,0
    elif value=="kurumsal":
        return 0,0,0,1,0,0,0,0
    elif value=="outsource":
        return 0,0,0,0,1,0,0,0
    elif value=="oyun":
        return 0,0,0,0,0,1,0,0
    elif value=="startup":
        return 0,0,0,0,0,0,1,0
    elif value=="yazTekn":
        return 0,0,0,0,0,0,0,1
    else:
        return 0,0,0,0,0,0,0,0

def setWorkType(value):
    if value=="geciciRem":
        return 1,0,0,0
    elif value=="hibrit":
        return 0,1,0,0
    elif value=="ofis":
        return 0,0,1,0
    elif value=="remote":
        return 0,0,0,1
    else:
        return 0,0,0,0

def setLocationType(value):
    if value=="yurtici":
        return 1
    else:
        return 0

def setCurrencyType(value):
    if value=="sterlin":
        return 1,0,0
    elif value=="tl":
        return 0,1,0
    elif value=="dolar":
        return 0,0,1
    else:
        return 0,0,0

def setGenderType(value):
    if value=="kadin":
        return 1
    else:
        return 0

	

	



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/statistics')
def statistics():
    return render_template("statistics.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/proje')
def proje():
    return render_template("proje.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/hesapla')
def hesapla():
    return render_template("model.html")


@app.route('/predict',methods=["POST"])
def predict():

    level = setLevelValues(request.form.get('level'))
    experience=setExperienceValues(request.form.get('experience'))
    cto,dataScience,dba,devopsEng,embeddedDev,frontend,fullStack,gameDev,mobileApp,others,qaTest,softwareArch,softwareManager,teamLead = setPositionValues(request.form.get('position'))
    gender = setGenderType(request.form.get('gender'))
    reklam,eticaret,finans,kurumsal,outsource,oyun,startup,yazTekn = setCompanyType(request.form.get('companyType'))
    geciciRem,hibrit,ofis,remote = setWorkType(request.form.get('workType'))
    locationType = setLocationType(request.form.get('location'))
    tl,dolar,euro = setCurrencyType(request.form.get('currency'))

   
   
    resultValues = np.array([[level,experience,cto,dataScience,dba,devopsEng,embeddedDev,frontend,fullStack,gameDev,mobileApp,others,qaTest,softwareArch,softwareManager,teamLead,gender,reklam,eticaret,finans,kurumsal,outsource,oyun,startup,yazTekn,geciciRem,hibrit,ofis,remote,locationType,tl,dolar,euro]])
   
    
    model=joblib.load('ml\gbm_final')
    pred=model.predict(resultValues)
   

    predictionValue=int(pred)
    text1="TL 'dir."
    
    return render_template('model.html', prediction_text=predictionValue,text=text1)

   

if __name__ == '__main__':
    app.run(debug=True)
