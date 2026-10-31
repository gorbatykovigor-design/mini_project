from django.shortcuts import render, get_object_or_404

from .models import Project, Skill



def home(request):
    return render(request, "index.html")




def all_project(request):
    projects = Project.objects.all()
    return render(request, 'my_project.html', {'projects': projects})



def get_project_detail(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'more_details.html', {'project': project})





def get_project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    return render(request, 'project_detail.html', {
        'project': project
    })



def pricing(request):
    return render(request, "pricing.html")



def about(request):
    return render(request, "about.html")



def expirience(request):
    return render(request, "expirience.html")


def skill(request):
    skills = Skill.objects.all()
    return render(request, "skills.html", {"skills": skills})







# Create your views here.
