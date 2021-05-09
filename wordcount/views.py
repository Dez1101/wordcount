from django.http import HttpResponse
from django.shortcuts import render
import operator 

def home(request):
    return render(request, 'home.html')

def count(request):
    fullText = request.GET['fullText']
    wordlist = fullText.split()
    wordDictionary = {}

    for word in wordlist:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    sortedWords = sorted( wordDictionary.items(),key=operator.itemgetter(1), reverse = True)
    return render(request, 'count.html',{'fullText': fullText, 'count':len(wordlist), 'sortedWords': sortedWords})
    
def about(request):
    return render(request, 'about.html')