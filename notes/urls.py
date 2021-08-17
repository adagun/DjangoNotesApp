from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('', views.index_view, name="index"),
   path('notes/', views.NotesView.as_view(), name="notes"),
   path('note/<int:pk>/', views.NoteView.as_view(), name="note"),
   path('edit_note/<int:pk>/', views.NoteEdit.as_view(), name="edit_note"),
   path('delete_note/<int:pk>/', views.NoteDelete.as_view(), name="delete_note"),
   path('create_note/', views.NoteCreate.as_view(), name="create_note"),
   path('login/', views.UserLoginView.as_view(), name="login"),
   path("logout/", LogoutView.as_view(next_page="index"), name="logout"),
   path("register/", views.RegistrationView.as_view(), name="register"),
 
   


]


       
        

