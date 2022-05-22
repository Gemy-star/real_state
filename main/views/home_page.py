from django.views import View
from django.shortcuts import render
from states.models import (
    Developers,
    Department,
    Projects,
)
from ..models import Blog


class HomePageView(View):
    def get(self, request):
        developers = Developers.objects.all().order_by('-pk')[:4]
        departments = Department.objects.all().order_by('-pk')[:6]
        projects = Projects.objects.all().order_by('-pk')[:12]
        blogs = Blog.objects.all().order_by('-pk')[:4]

        context = {
            "developers": developers,
            "departments": departments,
            "projects": projects,
            "blogs": blogs
        }
        return render(request, 'main/homepage/homepage.html', context=context)
