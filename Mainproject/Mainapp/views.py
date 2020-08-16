from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
# Create your views here.
def Index(request):
    return render(request, 'Mainapp/index.html')

def Register(request):


    return render(request, 'Mainapp/Register.html')

def Login(request):
    return render(request, 'Mainapp/Login.html')

def Reg_Done(request):
    db = sqlite3.connect('Registration')
    rs = db.cursor()

    #rs.execute('''create table Register(name varchar(50), email varchar(100), phone varchar(10), password varchar(10))''')
    #db.commit()
    rs.execute('''insert into Register values('shubh', '@gmail.com','1234567890', 'shubham1234#')''')
    db.commit()
    data = []
    rs.execute('select * from Register')
    for i in rs:
        data.append(i)
        print(i)

    return render(request, 'Mainapp/Reg_Done.html', {'data': data})