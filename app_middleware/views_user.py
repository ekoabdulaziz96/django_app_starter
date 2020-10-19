from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#--------------models
from .models import User as UserModel

#--------------forms
from .forms_user import UserForm
from .forms_user_super import SuperUserForm
from .forms_user_auth import UserAuthForm
from .forms_user_set_matkul import UserSetMatkulForm

#--------------views
from . import views
# from .bussiness_layer.access_control import AccessControl as AccessControlClass 

import numpy as np
import pandas as pd
import json
#---------------------------------------------------------------------extra_context
EC_user_listView = {
        'page_judul': 'Tabel User',
        'page_deskripsi': 'untuk mengelola User',
        'page_role': 'User',
    }

EC_user_createView= {
        'page_judul': 'Tambah User',
        'page_deskripsi': 'untuk menambah data User',
        'page_role': 'User',
        'role': 'create_user',
    }

EC_user_updateView = {
        'page_judul': 'Edit User',
        'page_deskripsi': 'untuk memperbarui data User',
        'page_role': 'User',
        'role': 'update_user',
    }

EC_superUser_createView= {
        'page_judul': 'Tambah User',
        'page_deskripsi': 'untuk menambah data User',
        'page_role': 'User',
        'role': 'create_super_user',
    }

EC_superUser_updateView = {
        'page_judul': 'Edit User',
        'page_deskripsi': 'untuk memperbarui data User',
        'page_role': 'User',
        'role': 'update_super_user',
    }

EC_userAuth_updateView ={
        'page_judul': 'Edit User',
        'page_deskripsi': 'untuk memperbarui data User',
        'page_role': 'User',
        'role': 'update',
    }

EC_user_detailView ={
        'page_judul': 'Detail User',
        'page_deskripsi': 'untuk melihat detail data User',
        'page_role': 'User'
    }
#----------------------------------------------------------------------------------------------Class view
#---------------------------------------------------------------------Read (list)
@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    model = UserModel
    ordering = ['id']
    template_name = "middleware/user/index.html"
    context_object_name = 'users'
    extra_context = EC_user_listView

    def get_queryset(self):
        queryset = self.model.objects.exclude(is_superuser=True)
        return queryset

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(UserListView, self).get_context_data(
            *args, **kwargs)

        return context
#-----------------------------------------------------------------------------------{{user}}
#---------------------------------------------------------------------Create
@method_decorator(login_required, name='dispatch')
class UserCreateView(SuccessMessageMixin, CreateView):
    # model UserModel
    form_class = UserForm
    template_name = "middleware/user/create.html"
    success_url = reverse_lazy('mw:user-index')
    context_object_name = 'forms'
    extra_context = EC_user_createView


    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(UserCreateView, self).get_context_data(
            *args, **kwargs)

        return context

    def get_success_message(self, cleaned_data):
        self.object.set_password(settings.DEFAULT_PASSWORD)
        self.object.save()

        return 'Data User berhasil ditambahkan'

#---------------------------------------------------------------------Update
@method_decorator(login_required, name='dispatch')
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = UserModel
    form_class = UserForm
    template_name = "middleware/user/create.html"
    context_object_name = 'users'
    success_url = reverse_lazy('mw:user-index')
    extra_context = EC_user_updateView
    
    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(UserUpdateView, self).get_context_data(
            *args, **kwargs)

        return context

    def get_success_message(self, cleaned_data):
        self.object.set_password(settings.DEFAULT_PASSWORD)
        self.object.save()
        return 'Data User berhasil diperbarui'

        

#---------------------------------------------------------------------Update Auth (profile)
@method_decorator(login_required, name='dispatch')
class UserUpdateAuthView(SuccessMessageMixin, UpdateView):
    model = UserModel
    form_class = UserAuthForm
    template_name = "middleware/user/create.html"
    context_object_name = 'users'
    success_url = reverse_lazy('index')

    extra_context = EC_userAuth_updateView
    
    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(UserUpdateAuthView, self).get_context_data(
            *args, **kwargs)

        return context

    def get_success_message(self, cleaned_data):
        # self.object.set_password(settings.DEFAULT_PASSWORD)
        # self.object.save()
        return 'Data User berhasil diperbarui'

#---------------------------------------------------------------------Delete
@method_decorator(login_required, name='dispatch')
class UserDeleteView(DeleteView):
    model = UserModel
    # template_name = "middleware/user/create.html"
    success_url = reverse_lazy('mw:user-index')
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        self.object.delete()
        return HttpResponseRedirect(success_url)

#---------------------------------------------------------------------Detail
@method_decorator(login_required, name='dispatch')
class UserDetailView(DetailView):
    model = UserModel
    template_name = "middleware/user/detail.html"
    context_object_name = 'user'
    extra_context = EC_user_detailView

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(UserDetailView, self).get_context_data(
            *args, **kwargs)
        context['list_matkul'] = self.get_object().matkul.all()

        return context

