# MADE BY ME
from django import http
from django.http import HttpResponse
from django.shortcuts import render
 


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('''<div style='background-color:skyblue'><h1>hello rex</h1><a
    # href='/about'>ABOUT----></a></div>''')

def about(request):
    text = request.POST.get('tex', 'NOT COOL')
    pun = request.POST.get('check', 'NO')
    cap = request.POST.get('check1', 'NO')
    low = request.POST.get('check11', 'NO')
    newline = request.POST.get('check2', 'NO')
    exspace = request.POST.get('check3', 'NO')
    countchar = request.POST.get('check4', 'NO')
    punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    def punk(t):
        text_t =''
        for i in t:
            if i not in punc:
                text_t += i
            # elif i==' ':
            #     text_t +=' ' 
        return text_t
    
    def capi(t):
        text_t =''
        for i in t:
            text_t += i.upper() 
        return text_t    
    
    def loki(t):
        text_t =''
        for i in t:
            text_t += i.lower() 
        return text_t

    def newl(t):
        # text_t =''
        # for i in t:
        #     if '\n' not in i:
        #         text_t += i
        return t

    def exsp(t):
        text_t =''
        for i,ch in enumerate(t):
            if not (t[i]==' ' and t[i+1]==' '):
                text_t += t[i]
        return text_t 

    if pun == 'on':
        para = {'msg':"Puctuations removed",'box':punk(text),'suc':'Success!'}
        text = punk(text)

    if cap == 'on':
        para = {'msg':"CAP is on",'box':capi(text),'suc':'Success!'}  
        text = capi(text)

    if low == 'on':
        para = {'msg':'Para in Lowercase','box':loki(text)}
        text = loki(text)

    if newline == 'on':     
        para = {'msg':'Newline removed','box1':newl(text),'suc':'Success!'}
        text = newl(text)

    if exspace == 'on':  
        if countchar == 'on':
                para = {'msg':f"Extra space removed & Number of characters is {len(capi(punk(text)))}",'box1':(text),'suc':'Success!'}
        else:   
            para = {'msg':'Extra space removed','box':exsp(text),'suc':'Success!'}
            return render(request, 'about.html', para)

    if countchar == 'on':  
        para = {'msg':f"Total {len(text)} Charcters",'box':text,'suc':'Success!'} 
        text = len(text)
    
    return render(request, 'about.html', para)
    # else:
    #     if len(text)!=0:
    #         para = {'msg':'None option selected','box':text,'suc':'Error!'} 
    #         return render(request, 'about.html', para)
    #     else:
    #         para = {'msg':'Empty Box','box':'Text box was empty','suc':'Error!'} 
    #         return render(request, 'about.html', para)



def setting(request):
    return HttpResponse('''<div style='background-color:gray'><h1>Inside Setting</h1><a 
    href='/about'><-----ABOUT</a><span>------------</span><a href='/profile'>PROFILE----></a></div>''')

def profile(request):
    return HttpResponse('''<div style='background-color:salmon'><h1>Inside Profile</h1><a 
    href='/setting'><-----SETTING</a><span>------------</span><a href='/'>HOME----></a></div>''')
