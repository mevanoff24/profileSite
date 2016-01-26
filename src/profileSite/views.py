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

# def pdf_view(request):
#     with open('static_in_pro/our_static/img/certificate.pdf', 'r') as pdf:
#         response = HttpResponse(pdf.read(), mimetype='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=scertificate.pdf'
#         return response
#     pdf.closed
