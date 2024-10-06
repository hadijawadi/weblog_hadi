from django.shortcuts import render,redirect
from .forms import Contact_form



def contact_view(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = Contact_form()
    return render(request,'contact_app/pages/contact.html',{'form':form})