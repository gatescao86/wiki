from django.shortcuts import render
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
                return entry(request, title)

        results = []
        for title in util.list_entries():
            if query in title and query != title:
                results.append(title)
        
        return render(request, "encyclopedia/search.html", {
            "results": results
        })

    return render(request, "encyclopedia/search.html")

def new_page(request):
    return render(request, "encyclopedia/new_page.html", {
        "form": NewEntryForm()
    })

