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
    text_t =''

# Remove punctuations
    def punk(t):
        text_t =''
        for i in t:
            if i not in punc:
                text_t += i
            # elif i==' ':
            #     text_t +=' ' 
        return text_t

#CAPTIALIZE
    def capi(t):
        text_t =''
        for i in t:
            text_t += i.upper() 
        return text_t    

#lowercase
    def loki(t):
        text_t =''
        for i in t:
            text_t += i.lower() 
        return text_t

#Remove newline
    def newl(t):
        # text_t =''
        # for i in t:
        #     if '\n' not in i:
        #         text_t += i
        return t

#Remove extra
    def exsp(t):
        text_t =''
        for i,ch in enumerate(t):
            if not (t[i]==' ' and t[i+1]==' '):
                text_t += t[i]
        return text_t 

#For punctuations
    if pun == 'on':
        if cap == 'on':
            if low == 'on':
                if newline == 'on':
                    if exspace == 'on':
                        if countchar =='on':
                            para = {'msg':f"Puctuations removed & CAP & LOW is on at the same time & New line removed & Extra space removed & Number of characters is {len(capi(punk(text)))}",'box1':f"Uppercase: {punk(capi(text))}\nLowercase: {punk(loki(text))}",'suc':'Success!'}
                        else: 
                            para = {'msg':f"Puctuations removed & CAP & LOW is on at the same time & New line removed & Extra space removed ",'box1':f"Uppercase: {newl(capi(text))}\nLowercase: {newl(loki(text))}",'suc':'Success!'}
                    else:
                        para = {'msg':f"Puctuations removed & CAP & LOW is on at the same time & New line removed ",'box1':f"Uppercase: {newl(capi(text))}\nLowercase: {newl(loki(text))}",'suc':'Success!'}
                elif exspace == 'on':
                    if countchar =='on':
                        para = {'msg':f"Puctuations removed & CAP & LOW is on at the same time & Extra space removed & Number of characters is {len(capi(punk(text)))}",'box1':f"Uppercase: {punk(capi(text))}\nLowercase: {punk(loki(text))}",'suc':'Success!'}
                    else: 
                        para = {'msg':f"Puctuations removed & CAP & LOW is on at the same time & Extra space removed ",'box1':f"Uppercase: {newl(capi(text))}\nLowercase: {newl(loki(text))}",'suc':'Success!'}
                elif countchar =='on':
                        para = {'msg':f"CAP & LOW is on at the same time & Number of characters is {len(capi(punk(text)))}",'box1':f"Uppercase: {punk(capi(text))}\nLowercase: {punk(loki(text))}",'suc':'Success!'}
                else:
                     para = {'msg':f"CAP & LOW & Puctuations removed ",'box':loki(punk(text)),'suc':'Success!'}
            elif newline == 'on':
                    if exspace == 'on':
                        if countchar == 'on':
                            para = {'msg':f"Puctuations removed & CAP is on & New line removed & Extra space removed & Number of characters is {len(capi(punk(text)))}",'box1':capi(punk(text)),'suc':'Success!'}
                        else:
                            para = {'msg':f"Puctuations removed & CAP is on & New line removed & Extra space removed ",'box1':capi(punk(text)),'suc':'Success!'}
                    else:       
                        para = {'msg':f"Puctuations removed & CAP is on & New line removed",'box1':capi(punk(text)),'suc':'Success!'}
            elif exspace == 'on':
                if countchar == 'on':
                        para = {'msg':f"Puctuations removed & CAP is on & Extra space removed & Number of characters is {len(capi(punk(text)))}",'box1':capi(punk(text)),'suc':'Success!'}
                else:
                        para = {'msg':f"Puctuations removed & CAP is on & Extra space removed ",'box1':capi(punk(text)),'suc':'Success!'}
            elif countchar == 'on':
                para = {'msg':f"CAP & Puctuations removed & Number of characters is {len(capi(punk(text)))}",'box':capi(punk(text)),'suc':'Success!'}
            else:
                para = {'msg':"CAP & Puctuations removed",'box':capi(punk(text)),'suc':'Success!'}  
            return render(request, 'about.html', para)

        elif low == 'on':
            if newline == 'on':
                    if exspace == 'on':
                        if countchar == 'on':
                            para = {'msg':f"Puctuations removed & low is on & New line removed & Extra space removed & Number of characters is {len(capi(punk(text)))}",'box1':loki(punk(text)),'suc':'Success!'}
                        else:
                            para = {'msg':f"Puctuations removed & low is on & New line removed & Extra space removed ",'box1':loki(punk(text)),'suc':'Success!'}
                    else:       
                        para = {'msg':f"Puctuations removed & low is on & New line removed",'box1':loki(punk(text)),'suc':'Success!'}      
            elif exspace == 'on':
                if countchar == 'on':
                    para = {'msg':f"Puctuations removed & low is on & Extra space removed & Number of characters is {len(capi(punk(text)))}",'box1':loki(punk(text)),'suc':'Success!'}
                else:
                    para = {'msg':f"Puctuations removed &  is on & Extra space removed ",'box1':loki(punk(text)),'suc':'Success!'}     
            elif countchar == 'on':
                para = {'msg':f"Puctuations removed & low is on & Number of characters is {len(capi(punk(text)))}",'box':loki(punk(text)),'suc':'Success!'}   
            else:
                para = {'msg':"LOW & Puctuations removed",'box':loki(punk(text)),'suc':'Success!'}
            return render(request, 'about.html', para)
        
        elif newline == 'on':
            if exspace == 'on':
                if countchar == 'on':
                     para = {'msg':f"Puctuations removed & New line removed & Extra space removed & Number of characters is {len(capi(punk(text)))}",'box1':(punk(text)),'suc':'Success!'}
                else:
                    para = {'msg':f"Puctuations removed & New line removed & Extra space removed ",'box1':(punk(text)),'suc':'Success!'}
            elif countchar == 'on':
                para = {'msg':f"Puctuations removed & New line removed & Number of characters is {len(capi(punk(text)))}",'box1':(punk(text)),'suc':'Success!'}
            else:       
                para = {'msg':f"Puctuations removed & New line removed",'box1':(punk(text)),'suc':'Success!'}
            return render(request, 'about.html', para)
        
        elif exspace == 'on':
            if countchar == 'on':
                para = {'msg':f"Puctuations removed & Extra space removed & Number of characters is {len(capi(punk(text)))}",'box1':(punk(text)),'suc':'Success!'}
            else:
                para = {'msg':f"Puctuations removed & Extra space removed ",'box1':(punk(text)),'suc':'Success!'}
            return render(request, 'about.html', para)

        elif countchar =='on':
            para = {'msg':f"Total {len(punk(text))} Charcters",'box':punk(text),'suc':'Success!'}
            return render(request, 'about.html', para)

        else:
            para = {'msg':"Puctuations removed",'box':punk(text),'suc':'Success!'}
            return render(request, 'about.html', para)
#For UPPERCASE
    elif cap == 'on':
        if low == 'on':
            if newline == 'on':
                if exspace == 'on':
                    if countchar =='on':
                        para = {'msg':f"CAP & LOW is on at the same time & New line removed & Extra space removed & Number of characters is {len(capi(punk(text)))}",'box1':f"Uppercase: {capi(text)}\nLowercase: {loki(text)}",'suc':'Success!'}
                    else: 
                        para = {'msg':f" CAP & LOW is on at the same time & New line removed & Extra space removed ",'box1':f"Uppercase: {newl(capi(text))}\nLowercase: {newl(loki(text))}",'suc':'Success!'}
                else:
                    para = {'msg':f"CAP & LOW is on at the same time & New line removed ",'box1':f"Uppercase: {newl(capi(text))}\nLowercase: {newl(loki(text))}",'suc':'Success!'}
            elif exspace == 'on':
                    if countchar =='on':
                        para = {'msg':f"CAP & LOW is on at the same time & Extra space removed & Number of characters is {len(capi(text))}",'box1':f"Uppercase: {capi(text)}\nLowercase: {loki(text)}",'suc':'Success!'}
                    else: 
                        para = {'msg':f" CAP & LOW is on at the same time & Extra space removed ",'box1':f"Uppercase: {newl(capi(text))}\nLowercase: {newl(loki(text))}",'suc':'Success!'}
            elif countchar =='on':
                        para = {'msg':f"CAP & LOW is on at the same time & Number of characters is {len(capi(punk(text)))}",'box1':f"Uppercase: {capi(text)}\nLowercase: {loki(text)}",'suc':'Success!'}
            else:
                para = {'msg':f"CAP & LOW is on at the same time",'box':f"Uppercase: {newl(capi(text))}\nLowercase: {newl(loki(text))}",'suc':'Success!'}
        
        elif newline == 'on':
                    if exspace == 'on':
                        if countchar == 'on':
                            para = {'msg':f"CAP is on & New line removed & Extra space removed & Number of characters is {len(capi(text))}",'box1':capi(text),'suc':'Success!'}
                        else:
                            para = {'msg':f"CAP is on & New line removed & Extra space removed ",'box1':capi(text),'suc':'Success!'}
                    else:       
                        para = {'msg':f"CAP is on & New line removed",'box1':capi(text),'suc':'Success!'}

        elif exspace == 'on':
            if countchar == 'on':
                para = {'msg':f"CAP is on & Extra space removed & Number of characters is {len(capi(text))}",'box1':capi(text),'suc':'Success!'}
            else:
                para = {'msg':f"CAP is on & Extra space removed ",'box1':capi(text),'suc':'Success!'}

        elif countchar == 'on':
            para = {'msg':f"CAP & Number of characters is {len(capi(text))}",'box':capi(text),'suc':'Success!'}

        else:
            para = {'msg':"CAP is on",'box':capi(text),'suc':'Success!'}  
        return render(request, 'about.html', para)
#For lowercase
    elif low == 'on':
        if newline == 'on':
            if exspace == 'on':
                if countchar == 'on':
                    para = {'msg':f"low is on & New line removed & Extra space removed & Number of characters is {len(capi(text))}",'box1':loki(text),'suc':'Success!'}
                else:
                    para = {'msg':f"low is on & New line removed & Extra space removed ",'box1':loki(text),'suc':'Success!'}
            else:       
                para = {'msg':f"low is on & New line removed",'box1':loki(text),'suc':'Success!'}      
        elif exspace == 'on':
            if countchar == 'on':
                para = {'msg':f"low is on & Extra space removed & Number of characters is {len(capi(text))}",'box1':loki(text),'suc':'Success!'}
            else:
                para = {'msg':f"low is on & Extra space removed ",'box1':loki(text),'suc':'Success!'}     
        elif countchar == 'on':
                para = {'msg':f"low is on & Number of characters is {len(text)}",'box':loki(text),'suc':'Success!'}   
        else:
            para = {'msg':'Para in Lowercase','box':loki(text)}
        return render(request, 'about.html', para)
#For newline
    elif newline == 'on':
        if exspace == 'on':
            if countchar == 'on':
                para = {'msg':f"New line removed & Extra space removed & Number of characters is {len(capi(punk(text)))}",'box1':(text),'suc':'Success!'}
            else:
                para = {'msg':f"New line removed & Extra space removed ",'box1':(text),'suc':'Success!'}
        elif countchar == 'on':
            para = {'msg':f"New line removed & Number of characters is {len(capi(punk(text)))}",'box1':(text),'suc':'Success!'}
        else:       
            para = {'msg':'Newline removed','box1':newl(text),'suc':'Success!'}
        return render(request, 'about.html', para)
#For extraspace
    elif exspace == 'on':  
        if countchar == 'on':
                para = {'msg':f"Extra space removed & Number of characters is {len(capi(punk(text)))}",'box1':(text),'suc':'Success!'}
        else:   
            para = {'msg':'Extra space removed','box':exsp(text),'suc':'Success!'}
            return render(request, 'about.html', para)
#For character count
    elif countchar == 'on':  
        para = {'msg':f"Total {len(text)} Charcters",'box':text,'suc':'Success!'} 
        return render(request, 'about.html', para)

    else:
        if len(text)!=0:
            para = {'msg':'None option selected','box':text,'suc':'Error!'} 
            return render(request, 'about.html', para)
        else:
            para = {'msg':'Empty Box','box':'Text box was empty','suc':'Error!'} 
            return render(request, 'about.html', para)

def setting(request):
    return HttpResponse('''<div style='background-color:gray'><h1>Inside Setting</h1><a 
    href='/about'><-----ABOUT</a><span>------------</span><a href='/profile'>PROFILE----></a></div>''')

def profile(request):
    return HttpResponse('''<div style='background-color:salmon'><h1>Inside Profile</h1><a 
    href='/setting'><-----SETTING</a><span>------------</span><a href='/'>HOME----></a></div>''')
