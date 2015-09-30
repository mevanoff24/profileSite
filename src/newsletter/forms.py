from django import forms

from .models import SignUp


class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)



class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email']

	def clean_email(self):
		email =  self.cleaned_data['email']
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data['full_name']
		return full_name