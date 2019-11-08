from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    totalcount = {}
    wordlist = fulltext.split()
    numwords = len(wordlist)
    uniquewords = set(wordlist)
    uniquewordslen = len(uniquewords)
    for i in range(len(wordlist)):
        if(wordlist[i] in totalcount):
            totalcount[wordlist[i]] +=  1
        else:
            totalcount[wordlist[i]] = 1
    tc = sorted(totalcount.items(), key=operator.itemgetter(1),reverse=True)

    return render(request, 'count.html', {'fulltext' : fulltext , 'numwords' : numwords, 'uniquewords' : uniquewordslen, 'totalcount' : tc})

def about(request):
    return render(request, 'about.html')
