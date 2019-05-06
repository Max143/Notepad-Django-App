from django import forms


class ContactForm(forms.Form):

	firstname = forms.CharField(required=False)
	lastname = forms.CharField(required=False)
	category = forms.ChoiceField(choices=[('Question', 'Question'), ('Other', 'Other')])
	email = forms.EmailField(label='Email')
	subject = forms.CharField(max_length=299)	
	message = forms.CharField(widget=forms.Textarea)

