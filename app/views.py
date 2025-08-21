from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import MyDataForm

def login_page(request):
    if request.method == 'POST':
        form = MyDataForm(request.POST)
        form_type = request.POST.get('form_type')
        
        if form.is_valid():
            # Process the valid form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            roll_number = form.cleaned_data['roll_number']
            password = form.cleaned_data['password']
            # Perform any other necessary actions with the form data
            # For example, save it to a database or perform other operations
            # Example: Save the form data to a database
            form.save()
            # messages.success(request, 'Form submitted successfully!')
            return redirect('success')
            
            if form_type == 'student':
                # Handle student logic
                pass
            elif form_type == 'admin':
                # Handle admin logic
                pass
        else:
            # Form has errors, they'll be displayed in the template
            return render(request, 'login.html', {'form': form})
    
    return render(request, 'login.html', {'form': MyDataForm()})

def success(request):
    """Display success page after form submission"""
    return render(request, 'home.html')