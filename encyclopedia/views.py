
from django.shortcuts  import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
import random
from markdown2 import Markdown
from . import util


class SearchForm(forms.Form):
    query = forms.CharField(label="Search Encyclopedia",required=False)


def index(request):
    form=SearchForm(request.POST)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), "form":form
    })
def page_view(request, title):
    form = SearchForm()
    entry = util.get_entry(title)
    if entry==None:
        return render(request, "encyclopedia/error.html", {
            "content":"No entry with such title, please try the search bar",
            "form":form
        })
    else:
        html_content = Markdown().convert(entry)
        #encyclopedia
        return render(request, "encyclopedia/page_view.html", {
            "content":html_content, "title":title,"form":form
        })

def search(request):
    if (request.method =="POST"):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            string = query.lower()
            entries = util.list_entries()
            list1 = list()
            exists = False
            if len(string)==0:
                return render(request, "encyclopedia/error.html", {
                "content":"Your search was empty please try again",
                "form":form
                })

            for  entry in entries:
                ent = entry.lower()
                if string==ent:
                    exists = True
                elif query in entry:
                    list1.append(entry)
            if(len(list1)==0):
                return render(request, "encyclopedia/error.html", {
                "content":"No entry with such title, please try the searching again",
                "form":form
                })
            if(exists==True):
                result = util.get_entry(query)
                page = Markdown().convert(result)
                return render(request, "encyclopedia/page_view.html", {
                "content":page, "title":result,"form":form
                })

            else:
                return render(request, "encyclopedia/index.html", {
                    "entries": list1, "form":form
                })






'''
def search(request):
    if (request.method =="POST"):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            string = query.lower()
            entries = util.list_entries()
            list1 = list()
            exists = False
            if len(string)==0:
                return render(request, "encyclopedia/error.html", {
                "content":"Your search was empty please try again",
                "form":form
                })

            for  entry in entries:
                if string==entry:
                    exists = True
                elif query in entry:
                    list1.append(entry)
            if(len(list1)==0):
                return render(request, "encyclopedia/error.html", {
                "content":"No entry with such title, please try the searching again",
                "form":form
                })
            elif(exists==True):
                query = util.get_entry(query)
                page = Markdown().convert(query)
                return render(request, "encyclopedia/page_view.html", {
                "content":page, "title":query,"form":form
                })

            else:
                return render(request, "encyclopedia/index.html", {
                    "entries": list1, "form":form
                })


'''
