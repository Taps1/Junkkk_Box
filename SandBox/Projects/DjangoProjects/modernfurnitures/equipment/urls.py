from django.conf.urls import url, include
from .views import ContactUs, Home, Gallery, AboutUs, Services


app_name = 'smp_site'
urlpatterns = [
    # url('', Home.as_view(), name='home'),     This will target all hits to home views.
    url('home/', Home.as_view(), name='home'),
    url('contact/', ContactUs.as_view(), name='contact'),
    url('services/', Services.as_view(), name='services'),
    url('gallery/', Gallery.as_view(), name='gallery'),
    url('about_us/',  AboutUs.as_view(), name='about_us'),
             ]
