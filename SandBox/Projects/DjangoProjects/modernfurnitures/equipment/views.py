# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from .models import PostMessage, ContactInfo
from .forms import ContactusForm
from django.shortcuts import render, redirect
from django.contrib import messages

class ContactUs(TemplateView):
    template_name = 'contact.html'

    def get(self, request):
        form = ContactusForm()
        contact_info = ContactInfo.objects.filter()
        return render(request, self.template_name, {'form': form, 'contact_info': contact_info})

    """def post(self, request):
        form = ContactusForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, 'has been saved  !!')
            # text = form.cleaned_data['post']
            # form = ContactusForm()
            # return HttpResponseRedirect('/contact_us/')
        else:
            form = ContactusForm()
        args = {'form': form}
        return render(request, self.template_name, args)"""


class Home(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        contact_info = ContactInfo.objects.all()
        return render(request, self.template_name, {'contact_info': contact_info})


class Gallery(TemplateView):
    template_name = 'gallery.html'

    def get(self, request):
        contact_info = ContactInfo.objects.all()
        return render(request, self.template_name, {'contact_info': contact_info})


class Mission(TemplateView):
    template_name = 'mission.html'

    def get(self, request):
        contact_info = ContactInfo.objects.all()
        return render(request, self.template_name, {'contact_info': contact_info})


class Subject(TemplateView):
    template_name = 'subjects.html'

    def get(self, request):
        contact_info = ContactInfo.objects.all()
        return render(request, self.template_name, {'contact_info': contact_info})
