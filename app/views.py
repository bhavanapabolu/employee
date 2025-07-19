from django.shortcuts import redirect, render 

from app.forms import EmployeeForm
from app.models import employee
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.
@login_required
def home(request):
    employees=employee.objects.all()
    return render(request,'app/home.html',{'employees':employees})
def detail(request,id):
    employee1=employee.objects.get(id=id)
    return render(request,'app/employee_detail.html',{'employee1':employee1})
def add_employee(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_success')
    else:   
        form=EmployeeForm()
    return render(request,'app/add_employee.html',{'form':form})
def success_view(request):
    return render(request,'app/success.html')
def register(request):
    if request.method=='POST':
       form=UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('login')
    else:
         form=UserCreationForm()
    return render(request,'app/register.html',{'form':form})
