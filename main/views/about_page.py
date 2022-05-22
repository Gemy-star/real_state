from django.views.generic import View
from django.shortcuts import render


class AboutPageView(View):
    def get(self, request):
        return render(request, 'main/aboutpage/about.html')
