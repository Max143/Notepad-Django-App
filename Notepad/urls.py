from django.urls import path, re_path
from . import views


urlpatterns = [
    path('notepad/', views.NotepadView, name='notepad'),

    # My Notepad view
    path('notepad/mynotes/', views.MyNoteView, name='notepadview'),

    # Create Notepad View
    path('notepad/create/', views.CreateView, name='createview'),

    # Detail View of Note
    path('notepad/mynotes/details/<id>', views.DetailView, name='detailview'),

    # Edit View
    path('notepad/mynotes/edit/<id>', views.EditView, name='editview'),

    # Update View
    path('notepad/mynotes/update/<id>', views.UpdateView, name='detailview'),

    # Delete View
    path('notepad/mynotes/<id>/delete', views.DeleteView	, name='detailview'),



    
]
