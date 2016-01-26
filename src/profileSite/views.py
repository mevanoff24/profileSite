from django.shortcuts import render

def about(request):
		page = 'about.html'
		context = {}
		return render(request, page, context)


def resume(request):
		page = 'resume.html'
		context = {}
		return render(request, page, context)


def certificates(request):
		page = 'certificates.html'
		context = {}
		return render(request, page, context)


def blog(request):
		page = 'blog.html'
		context = {}
		return render(request, page, context)


