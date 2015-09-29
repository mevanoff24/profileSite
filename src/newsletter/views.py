from django.shortcuts import render

# Create your views here.
def home(request):
	page = 'home.html'
	context = {}
	return render(request, page, context)