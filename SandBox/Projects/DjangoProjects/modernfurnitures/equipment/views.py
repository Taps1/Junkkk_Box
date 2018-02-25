# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from .models import ContactInfo
from .forms import ContactusForm
from django.shortcuts import render, redirect
from django.contrib import messages

class Home(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        contact_info = ContactInfo.objects.all()
        return render(request, self.template_name, {'contact_info': contact_info})

class AboutUs(TemplateView):
    template_name = 'about_us.html'

    def get(self, request):
        contact_info = ContactInfo.objects.all()
        return render(request, self.template_name, {'contact_info': contact_info})


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

class Gallery(TemplateView):
    template_name = 'gallery.html'

    def get(self, request):
        contact_info = ContactInfo.objects.all()
        return render(request, self.template_name, {'contact_info': contact_info})


class Services(TemplateView):
    template_name = 'services.html'

    def get(self, request):
        contact_info = ContactInfo.objects.all()
        return render(request, self.template_name, {'contact_info': contact_info})
