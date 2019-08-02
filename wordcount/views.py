from django.http import HttpResponse
from django.shortcuts import render
import operator
import re

def home(request):
    return render(request, 'home.html')

def count (request):
    fulltext=request.GET['fulltext']
    print(fulltext)
    wordlist=re.findall('[^-., ]+',fulltext)

    wordcounter_1=dict()
    for word in wordlist:
        wordcounter_1[word]=wordcounter_1.get(word,0)+1

    sorted_words=sorted(wordcounter_1.items(),key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'sortedwords':sorted_words})

def about(request):
    return render(request, 'about.html')
