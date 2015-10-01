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
