from django.shortcuts import render
from django.views.generic import TemplateView
from .models import CarouselImage


class HomeView(TemplateView):
    template_name = 'home/homepage.html'

    def get_context_data(self, **kwargs):
        carousel_images = CarouselImage.objects.all()
        context = {
            'carousel_images': carousel_images,
        }
        return context


class AboutView(TemplateView):
    template_name = 'home/about.html'


class ContactView(TemplateView):
    template_name = 'home/contact.html'
