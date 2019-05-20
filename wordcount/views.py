from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')
def count(request):
    text=request.GET['words']
    wordlist=text.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word]=1
    sortedDictionary=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'words': text, 'count': len(wordlist),'sortedDictionary': sortedDictionary})