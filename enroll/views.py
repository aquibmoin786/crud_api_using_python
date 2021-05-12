from django.shortcuts import render,HttpResponseRedirect
from .forms import EmployeeRegistration
from .models import User
# Create your views here.

# This Function will Add new Item and Show All Items
def add_show(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = EmployeeRegistration()
    else:
        fm = EmployeeRegistration()
    stud = User.objects.all()    
    return render(request, 'enroll/addandshow.html',{'form':fm,
    'stu':stud})
# This function will be update or Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(instance=pi)
                
    return render(request, 'enroll/updateemployee.html',{'form':fm})



# This Function will Delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')    