from django import forms

class NameForm(forms.Form):

    # get from vehicle_type
    MAKE_CHOICE = [('none', '------'),('bmw', 'BMW'), ('hyundai', 'Hyundai'), ('honda', 'Honda')]
    # implement dependent drop down list using model classes | this one is for bmw
    MODEL_CHOICE = [('none', '------'), ('x5','X5'), ('i8', 'i8'), ('7series', '7 Series')]

    Name = forms.CharField(label='Name')
    Address = forms.CharField()
    Phone_Number = forms.CharField()
    Pick_Up_Location = forms.CharField(label='Pick Up Location')
    Pick_Up_Time = forms.CharField(label='Pick Up Time') # could be a dropdown list
    Car_Make = forms.CharField(label='Select Car Model:', widget=forms.Select(choices=MAKE_CHOICE))
    Car_Model = forms.CharField(label='Select Car Model:', widget=forms.Select(choices=MODEL_CHOICE))