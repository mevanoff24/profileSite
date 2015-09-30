from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import SignUpForm, ContactForm
from .models import SignUp

# Create your views here.
def home(request):
	title = 'Sign Up Now'
	if request.user.is_authenticated:
		title = 'Hello {}'.format(request.user)

	page = 'home.html'

	context = {
		'title':title,
	}
	return render(request, page, context)


def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data['email']
		form_message = form.cleaned_data['message']
		form_full_name = form.cleaned_data['full_name']
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		
		contact_message = "{}: {} via {}".format(form_full_name, form_message, form_email)

		send_mail(subject, 
			contact_message, 
			from_email, 
			[to_email], 
			fail_silently=True)

	context = {
		'form': form,
		'title': title,
		'title_align_center': title_align_center,
	}

	return render(request, 'forms.html', context)


