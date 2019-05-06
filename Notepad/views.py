from django.shortcuts import render, redirect, get_object_or_404
from .forms import NotepadForm
from django.contrib import messages
from .models import Notepad
# Decorators add functionality 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def NotepadView(request):
	return render(request, 'notepad/notepad.html')



# Notepad View
@login_required
def MyNoteView(request):
	my_notes = Notepad.objects.all()
	paginator = Paginator(my_notes, 4)
	context = {'my_notes':my_notes}
	return render(request, 'notepad/mynotes.html', context)


# Detail View of Each Noteid
@login_required
def DetailView(request, id):
	try:
		note = Notepad.objects.get(id=id)
	except Notepad.DoesNotExist:
		raise Http404("No Note Exist here !")
	return render(request, 'notepad/detail.html', {'note':note})


# Create View
@login_required
def CreateView(request):
	if request.method == 'POST':
		form = NotepadForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Note saved Successfully !')
			return redirect('notepadview')
	else:
		form = NotepadForm()
		return render(request, 'notepad/create.html', {'form': form})

'''
# Edit View
def EditView(request, id):
	note = Notepad.objects.filter(id=id)
	context = {'note': note}
	return render(request, 'notepad/edit.html', context)''=
'''
@login_required
def EditView(request, id):
	note = get_object_or_404(Notepad, pk=id)
	if request.method == 'POST':
		form = NotepadForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
			messages.success(request, 'Note had been successfully edited !')
			return redirect('notepadview')
	else:
		form = NotepadForm(instance=note)
		context = {'form':form}
	return render(request, 'notepad/edit.html', context)


# Update View
@login_required
def UpdateView(request, id):
	note = Notepad.objects.get(id=id)
	note.title = request.method['title']
	note.description = request.method['description']
	note.save()
	return redirect('notepadview')


# Delete View
@login_required
def DeleteView(request, id):
	note = Notepad.objects.filter(id=id)
	note.delete()
	return redirect('notepadview')

