from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Note
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import NoteForm
# Create your views here.



def index_view(request):
    return render(request, 'base/index.html')


class NotesView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/notes.html"
    
    # only let the logged in user see their own notes
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notes"] = context["notes"].filter(user=self.request.user)
        return context
        
class NoteView(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = "note"
    template_name = "notes/note.html"


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    # send back to notes page
    success_url = reverse_lazy('notes')
    template_name ="notes/note_form.html"
    
    # the notes is created for the logged in user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreate, self).form_valid(form)

class NoteEdit(LoginRequiredMixin, UpdateView):
    model = Note    
    form_class = NoteForm
    success_url = reverse_lazy('notes')
    template_name ="notes/note_form.html"

class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    context_object_name = 'note'
    success_url = reverse_lazy('notes')
    template_name ="notes/delete_note.html"



class UserLoginView(LoginView):
    template_name = "auth/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('notes')
class RegistrationView(FormView):
    template_name = "auth/register.html"
   
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistrationView, self).form_valid(form)

    # redirect to notes page if already logged in
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes')
        return super(RegistrationView, self).get(*args, **kwargs)
