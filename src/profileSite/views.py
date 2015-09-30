from django.shortcuts import render

def about(request):
		page = 'about.html'
		context = {}
		return render(request, page, context)

		