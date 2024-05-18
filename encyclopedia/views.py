from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from . import util

class NewEntryForm(forms.Form):
    entry = forms.CharField(label="Title")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title),
        "title": title 
    })

def search(request):
    if request.method == "POST":
        query = request.POST['q']

        for title in util.list_entries():
            if query == title:
                # return entry(request, title)
                return HttpResponseRedirect('/entry/' + title)

        results = []
        for title in util.list_entries():
            if query in title and query != title:
                results.append(title)
        
        return render(request, "encyclopedia/search.html", {
            "results": results
        })

    return render(request, "encyclopedia/search.html")

def create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        if title in util.list_entries():
            return HttpResponseRedirect('/error')
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect('/entry/' + title)
    
    return render(request, "encyclopedia/create.html")

def error(request):
    return render(request, "encyclopedia/error.html")

def edit(request, title):
    if request.method == "GET":
        content = util.get_entry(title)

        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
    
    elif request.method == "POST":
        content = request.POST['content']
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("wiki:entry", kwargs={'title': title}))

    return render(request, "encyclopedia/edit.html")

def random(request):
    pass
