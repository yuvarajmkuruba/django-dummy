from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def  index(request):
    # return HttpResponse(
    #     '<h1>Hey ,Welcome</h1>\n <p>Hello King</p> <h2>Hey</h2><h2>Done</h2><a href="http://www.camfyvision.com">Camfy</a>'
    #     )
    # name ='john'
    # context1={
    #     'name': 'king',
    #     'age' : 23,
    #     'nationality':'indian'
    # }
    return render(request,'index.html')
def counter(request):
    num1=request.POST['num1']
    num2=request.POST['num2']
    oper=request.POST['operator']
    # amo=len(hey1.split())
    def add(num1,num2,oper):
        if(oper=='+'):
            return num1+num2
        elif (oper=='-'):
             return num1-num2
        elif (oper=='*'):
             return num1*num2 
        elif (oper=='/'):
             return round(num1/num2)    
    cou=add(int(num1),int(num2),oper)
    return render(request,'counter.html',{ 'final':cou})
def counter1(request):
    hey1=request.GET['hey1']
    # nw=len(tex1.split())
    amo=len(hey1.split())
    return render(request ,'counter1.html',{'val':amo})
def counter2(request):
    num1=request.POST['num1']
    num2=request.POST['num2']
    oper=request.POST['operator']
    def add(num1,num2,oper):
        if(oper=='+'):
            return num1+num2
        elif (oper=='-'):
             return num1-num2
        elif (oper=='*'):
             return num1*num2 
        elif (oper=='/'):
             return round(num1/num2)    
    cou=add(int(num1),int(num2),oper)
    hey1=request.POST['laa']
    amo=len(hey1.split())
    return render(request ,'counter2.html',{'val':amo,'final':cou})