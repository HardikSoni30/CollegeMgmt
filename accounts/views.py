from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, FormView, UpdateView
from .forms import (UserCreationForm, UserLoginForm,
                    StudentProfileForm, StaffProfileForm)
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy


# Create your views here.
from .models import StudentProfile, StaffProfile


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:login')


class SignInView(FormView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        request = self.request
        # print(request.user.is_authenticated)
        next_ = request.GET.get('next')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
        # print(user)
        # print(request.user.is_authenticated)
        if user is not None:
            login(request, user)
            # print(request.user.is_authenticated)
            return redirect('home')
        else:
            messages.error(request, 'The e-mail address and/or password you specified are not correct.')
            # return redirect('login')
            return super(SignInView, self).form_invalid(form)


class StaffProfileView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    form_class = StaffProfileForm
    # success_url = reverse_lazy('home')
    success_message = "Profile Updated Successfully"

    def get_object(self, queryset=None):
        user_id = self.kwargs.get("user_id")
        return get_object_or_404(StaffProfile, user_id=user_id)


class StudentProfileView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    form_class = StudentProfileForm
    # success_url = reverse_lazy('home')
    success_message = "Profile Updated Successfully"

    def get_object(self, queryset=None):
        user_id = self.kwargs.get("user_id")
        return get_object_or_404(StudentProfile, user_id=user_id)

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     image = form.cleaned_data.get('profile_pic')
    #     print(image)
    #     if form.is_valid():
    #         messages.success(self.request, "Profile Updated Successfully")
    #         super(StudentProfileView, self).form_valid(form)
    #         return HttpResponseRedirect(self.get_success_url())
    #     else:
    #         messages.error(self.request, 'something is not correct')
    #         # return redirect('login')
    #         return super(StudentProfileView, self).form_invalid(form)
