from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    djtext= request.POST.get('text', "default")

    removepunc= request.POST.get('removepunc', "off")
    fullcap= request.POST.get('fullcap', "off")
    newlineremover= request.POST.get('newlineremover', "off")
    extraspaceremover= request.POST.get('extraspaceremover', "off")

    charactercounter= request.POST.get('charactercounter', "off")
    strr = djtext
    purpose=""    

    if removepunc == 'on':
        analyzed=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed + char
        params ={'purpose': 'Removed Punctuation', 'analyzed_text':analyzed}
        strr = analyzed
        purpose += "| Removed Punctuations"

    if fullcap=="on":
        strr = strr.upper()
        print(strr)
        params ={'purpose': 'UPPERCASE', 'analyzed_text':strr}
        purpose += "| UPPERCASE "

    if newlineremover=='on':
        analyzed=""
        for char in strr:
            if char != "\n" and char !='\r':
             analyzed= analyzed + char
        params ={'purpose': 'New Line Removed', 'analyzed_text':analyzed}
        strr=analyzed
        purpose += "| New Line removed"

    if extraspaceremover=='on':
        analyzed=""
        for index, char in enumerate(strr):
            if not(strr[index]== "" and strr[index+1]=="") :            
             analyzed= analyzed + char
        params ={'purpose': 'Extra Space Removed', 'analyzed_text':analyzed}
        strr=analyzed
        purpose += "| Extra Space Removed "

    if charactercounter=="on":
        analyzed=''
        for char in strr:
            analyzed= len(strr)
        params ={'purpose': 'Character counted', 'analyzed_text':analyzed}
        strr=analyzed
        purpose += "| Character counted"
    params ={'purpose':purpose, 'analyzed_text':strr}
    
    if removepunc =='on' or fullcap =='on' or extraspaceremover =='on' or newlineremover =='on' or charactercounter=='on':
         return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error! Please Select an operation.")   
