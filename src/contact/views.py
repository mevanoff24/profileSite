from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


from .forms import ContactForm

# Create your views here.

def contact(request):
	title = 'Contact Me'
	form = ContactForm(request.POST or None)
	context = {
		'title': title,
		'form': form,
	}

	if form.is_valid():
		comment = form.cleaned_data['comment']
		name = form.cleaned_data['name']
		subject = 'Message from MYSITE.com'
		message = '%s %s' %(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
		title = 'Thanks'
		confirm_message = 'Thanks for the message'
		context = {
			'title': title,
			'confirm_message': confirm_message
		}
	# context = locals()
	page = 'contact.html'
	return render(request, page, context)
