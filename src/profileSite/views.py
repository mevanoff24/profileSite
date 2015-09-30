from django.shortcuts import render

def about(request):
		page = 'about.html'
		context = {}
		return render(request, page, context)


def resume(request):
		page = 'resume.html'
		context = {}
		return render(request, page, context)

