from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already taken')
                return redirect('register')
            else:
                # Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already taken')
                    return redirect('register') 
                else:
                    # create user
                    user = User.objects.create_user(
                        username=username,
                        first_name= first_name,
                        last_name= last_name,
                        email=email,
                        password=password
                    )
                    user.save()

                    messages.success(request, 'registred successfully, you can login now')
                    return redirect('register')

        else:
            messages.error(request, 'Passwords don\'t match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')
