from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    count = len(wordlist)
    if(count == 1):
        text_one = 'is'
        text_two = 'word'
    else:
        text_one = 'are'
        text_two = 'words'

    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sortwords = sorted(word_dict.items(), key= operator.itemgetter(1), reverse = True)
    return render(request, 'count.html',{'fulltext':fulltext,'count':count
                                         ,'text_one':text_one,'text_two':text_two,'sortwords':sortwords})