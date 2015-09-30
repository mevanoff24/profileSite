from django.shortcuts import render

# Create your views here.

def projects(request):
		page = 'projects.html'
		context = {}
		return render(request, page, context)

