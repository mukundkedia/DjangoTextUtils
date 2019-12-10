# i hv created
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    removepunc =  request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcount','off')

    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps=="on":
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover=="on":
        analyzed=""
        for a in djtext:
            if a!="\n" and a!="\r":
                analyzed = analyzed + a

        params = {'purpose': 'Remove newline', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcounter=="on":
        analyzed = len(djtext)

        params = {'purpose': 'Total Characters', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removepunc!="on" and charcounter!="on" and extraspaceremover!="on" and fullcaps!="on" and newlineremover!="on"):
        return HttpResponse("error")


    return render(request,'analyze.html',params)

