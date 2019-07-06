from django.http import HttpResponse
from django.shortcuts import render

def home(request):

	return render(request, "home.html")

def count(request):

	fulltext = request.GET["fulltext"]
	wordlist = fulltext.split()
	word_dict = {}

	for word in wordlist:
		if word not in word_dict:
			word_dict[word] = 1
		else:
			word_dict[word] += 1

	return render(request, "count.html", {"fulltext":fulltext, "number_of_words":len(wordlist)})

def about(request):

	return render(request, "about.html")