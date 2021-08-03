from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from D2R.users.forms import LoginForm, RegisterForm, UserProfileForm
from D2R.users.models import Profile


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.user_cache
            login(request, user)
            return redirect('home')
        else:
            context = {
                'form': form,
            }

            return render(request, 'login.html', context=context)
    else:
        form = LoginForm()
        context = {
            'form': form,
        }

        return render(request, 'login.html', context=context)


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

        else:
            context = {
                'form': form,
            }

            return render(request, 'register.html', context=context)
    else:
        form = RegisterForm()
        
        context = {
            'form': form,
        }

        return render(request, 'register.html', context=context)


@login_required()
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def profile_user(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile user')
    else:

        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'user-profile.html', context=context)
