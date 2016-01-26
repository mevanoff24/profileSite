from django.shortcuts import render

# Create your views here.

def projects(request):
		page = 'projects.html'
		context = {}
		return render(request, page, context)


def sabermetrics(request):
		page = 'sabermetrics.html'
		context = {}
		return render(request, page, context)

def nycsubway(request):
		page = 'nycsubway.html'
		context = {}
		return render(request, page, context)

def playoffprediction(request):
		page = 'playoffprediction.html'
		context = {}
		return render(request, page, context)

def enron(request):
		page = 'enron.html'
		context = {}
		return render(request, page, context)

def customersegmentation(request):
		page = 'customersegmentation.html'
		context = {}
		return render(request, page, context)

def twittersentiment(request):
		page = 'twittersentiment.html'
		context = {}
		return render(request, page, context)

def stockanalysis(request):
		page = 'stockanalysis.html'
		context = {}
		return render(request, page, context)

def movierecommendation(request):
		page = 'movierecommendation.html'
		context = {}
		return render(request, page, context)

def sfcrime(request):
		page = 'sfcrime.html'
		context = {}
		return render(request, page, context)




