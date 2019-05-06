from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError  # for security reason
# Decorators add functionality 
from django.contrib.auth.decorators import login_required 
import smtplib



# Sending Email to Terminal or server Terminal :
# And also sending User
@login_required 
def ContactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
				firstname = form.cleaned_data['firstname']
				lastname = form.cleaned_data['lastname']
				email = form.cleaned_data['email']
				subject  = form.cleaned_data['subject']
				message = form.cleaned_data['message']

				# setting Up the Server
				host = 'smtp.gmail.com'
				port = 587

				support_mail_id = 'aoen143@gmail.com'
				support_password = '@emmawatson143@'

				# Email Connnection to server
				email_conn = smtplib.SMTP(host, port)

				email_conn.ehlo()  # can be omitted

				# Now connecting a secured layer
				email_conn.starttls()

				# Login into Support Mail
				email_conn.login(support_mail_id, support_password)

				
				#send = "First Name :" + firstname + "Last Name: " + lastname + ". Email: " + email + ". subject: " + subject + "Message: " + message+ "."
				from_email = email
				to_email = support_mail_id
				test = "Dummy Msg 3"
				# Sending Email with Error Handling
				try :
					email_conn.sendmail(from_email, to_email, test)
				except BadHeaderError:
					return HttpResponse('Invalid header found !')


				try:
					send_mail(subject, message, email, ['aoen143@gmail.com'])
				except BadHeaderError:
					return HttpResponse('Invalid header found !')

				#print(firstname, lastname , email, subject, message)
				messages.success(request, f'Query Sent Successfully !')
				return render(request, 'contact/sent.html')
	else:
		if request.method == 'GET':
			form = ContactForm()
			context = {'form': form}
			return render(request, 'contact/contact.html', context)


'''
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

'''