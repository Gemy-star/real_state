from django.views import View
from django.shortcuts import render
from states.models import (
    Developers,
    Department
)


class HomePageView(View):
    def get(self, request):
        developers = Developers.objects.all().order_by('-pk')[:4]
        departments = Department.objects.all().order_by('-pk')[:6]
        context = {
            "developers": developers,
            "departments": departments
        }
        return render(request, 'main/homepage/homepage.html', context=context)
