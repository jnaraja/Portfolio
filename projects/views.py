from django.shortcuts import render, get_object_or_404

from .models import Project, Resume


# Create your views here.
def home(request):
    projects = Project.objects
    resumes = Resume.objects
    return render(request, 'projects/home.html', {'projects':projects, 'resume':resumes})

def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk = project_id)
    return render(request, 'projects/detail.html', {'project':project_detail})

def csv(request, csv_id):
    csv_file = get_object_or_404(Project, pk = csv_id)
    return render(request, 'projects/csv.html', {'csv':csv_file})