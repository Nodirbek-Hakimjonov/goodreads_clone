from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from users.forms import UserCreateForm, UserLoginForm,UserUpdateForm


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm
        context = {
            'form': create_form
        }
        return render(request, template_name='users/register.html', context=context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            return render(request, template_name='users/register.html', context=context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, template_name='users/login.html', context={'login_form': login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request,'you successfully logged in')
            return redirect('books:list')
        else:

            return render(request, template_name='users/login.html', context={"login_form": login_form})
class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        if not  request.user.is_authenticated:
            return redirect('users:login')
        return render(request,template_name='users/profile.html',context={'user':request.user})

class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.info(request,'you successfully logged out.')
        return redirect('landing_page')

class ProfileEditView(LoginRequiredMixin,View):
    def get(self,request):
        user_update_form=UserUpdateForm(instance=request.user)
        return render(request,'users/profile_edit.html',{'form':user_update_form})
    def post(self,request):
        user_update_form=UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request,'You have successfully updated your profile.')

            return redirect('users:profile')
        return render(request,'users/profile_edit.html.html',{'form':user_update_form})
