from django.shortcuts import render
from django.http import HttpResponse
from . import forms
def index(request):
    my_dict = {'insert_me': 'Hello I am from views.py!'}
    return render(request, '../templates/index.html', context=my_dict)

class Form:
    def getForm(request):
        form = forms.NameForm()
        if request.method == 'POST':
            form = forms.NameForm(request.POST)
            if form.is_valid():
                # post changes on customer, reservation, transport_phase, assigned
                print('DATA: '+ form.cleaned_data['Car_Make'])


        return render(request, 'post/form_page.html', {'form': form})
