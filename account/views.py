from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib import messages
from django.urls import reverse
# Create your views here.
def Signup(request):
    if request.method == 'POST':
        # Extract form data
        user_type = request.POST.get('user_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        profile_picture = request.FILES.get('profile_picture')
        address = request.POST.get('address')

        user = User.objects.filter(username=username)
        if user:
            messages.warning(request, 'User already exist !')
            return redirect('signup')

        else:
            if password1 == password2:
                new_user = User.objects.create(user_type=user_type, first_name=first_name, last_name=last_name,
                                                     username=username, email=email, password=password1,
                                                     profile_picture=profile_picture,
                                                     address=address)
                request.session['registration_complete'] = True

                return redirect('register_success')

            else:
                messages.error(request, 'Password does not match with confirm password')
                return redirect('signup')

    return render(request, 'signup.html', )


def Login(request):
    if request.method == "POST":
        user_type = request.POST.get('user_type')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        try:
            user = User.objects.get(username=username)
            if user.password == password1:
                request.session['user_id'] = user.id
                request.session['registration_complete'] = True
                return redirect('dashboard')
            else:
                messages.error(request, 'Wrong password')
                return redirect('login')

        except:
            messages.warning(request, "No User exist Register first ")
            return redirect('login')
    return render(request, "login.html")


def success_register(request):
    if request.session.get('registration_complete', False):
        return render(request, 'registered.html')
    else:
        return redirect('signup')


def Dash(request):
    if request.session.get('registration_complete', False):
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        img = user.profile_picture.url

        return render(request, "dash.html", {'author': user, 'img': img })
    else:
        return redirect('signup')


def Logout(request):
    request.session['registration_complete'] = False
    return render(request, "logout.html")

