from django.shortcuts import render
#from .forms import UserCreationEmailForm
from django.contrib.auth.forms import UserCreationForm

def signup(request):
	#form = UserCreationEmailForm()
	form = UserCreationForm(request.POST or None)

	if form.is_valid():
		form.save()
	return render(request, 'signup.html',{'form':form})