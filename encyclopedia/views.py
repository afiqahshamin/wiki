from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wikipage(request, title):
	if util.get_entry(title) == None:
		return render(request, "encyclopedia/error.html", {
			"title": title.capitalize()
		})
	else:
		return render(request, "encyclopedia/wikipage.html", {
			"content": util.get_entry(title),
			"title": title.upper()
		})