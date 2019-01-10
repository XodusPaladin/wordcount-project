# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 23:09:22 2019

@author: cawri
"""

#from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


def count(request):
    fulltext = request.GET["fulltext"]
    
    mydictionary = {}
    
    wordlist = fulltext.split()
    for word in wordlist:
        if word in mydictionary:
            mydictionary[word] +=1
        else:
            mydictionary[word] = 1
            
            
    sortedlist=sorted(mydictionary.items(), key=operator.itemgetter(1),reverse=True)
    
    return render(request, "count.html",{"fulltext":fulltext,"wordcount":len(wordlist), 
                                         "sortedlist":sortedlist})
