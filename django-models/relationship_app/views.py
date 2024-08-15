from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Book 
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
def list_books(request):
   
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to a view after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # Redirect to a view after login
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')



class LibraryDetailView(DetailView):
 
    model = Library
  
    template_name = 'relationship_app/library_detail.html'

    context_object_name = 'library'

    def get_context_data(self, **kwargs):
     
        context = super().get_context_data(**kwargs)
       
        context['books'] = self.object.books.all() 
        return context
