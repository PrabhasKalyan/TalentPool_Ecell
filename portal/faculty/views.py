from django.shortcuts import render
from .models import Faculty,Intern
from django.db.models import Q
import json
from urllib.parse import unquote_plus

def blog1(request):
    return render(request, 'faculty/blog1.html')

def blog2(request):
    return render(request, 'faculty/blog2.html')

def blog3(request):
    return render(request, 'faculty/blog3.html')

def blog4(request):
    return render(request, 'faculty/blog4.html')

def blog5(request):
    return render(request, 'faculty/blog5.html')



def search(request):
    query = request.GET.get('query', None)
    university = request.GET.get('org', None)
    area = request.GET.get('profile', None)

    All_Faculties = Faculty.objects.all()

    all_interns = Intern.objects.all()

    if query:
        interns = (Intern.objects.filter(Q(name_of_org__icontains=query)) | 
                     Intern.objects.filter(Q(profiles__icontains=query)) | 
                     Intern.objects.filter(Q(location__icontains=query)) | 
                     Intern.objects.filter(Q(job_description__icontains=query))) 
    else:
        interns = all_interns
    if university and area:
        interns = all_interns.filter(name_of_org__icontains=unquote_plus(university),
                                     profiles__icontains=unquote_plus(area))
    elif university:
        interns = all_interns.filter(name_of_org__icontains=unquote_plus(university))
    elif area:
        interns = all_interns.filter(profiles__icontains=unquote_plus(area))
    else:
        interns = all_interns


    all_profiles=set()
    for intern in all_interns:
        profile=getattr(intern,'profiles')
        for pro in profile:
            all_profiles.add(pro)

    all_orgs=set()
    for intern in all_interns:
        org=getattr(intern,'name_of_org')
        all_orgs.add(org)

    all_profiles = sorted(all_profiles)
    all_orgs = sorted(all_orgs)

    context = {
        'Faculties': interns,
        'research_areas': all_profiles,
        'colleges': all_orgs,
    }

    return render(request, 'faculty/search.html', context)

def professor(request, name_of_org):
    id = request.GET.get('id', None)
    intern = Intern.objects.get(id = id)

    context = {
        'internship': intern,
    }

    return render(request, 'faculty/professor.html', context)

def home(request):
    interns = Intern.objects.all()

    all_profiles=set()
    for intern in interns:
        profile=getattr(intern,'profiles')
        for pro in profile:
            all_profiles.add(pro)

    all_orgs=set()
    for intern in interns:
        org=getattr(intern,'name_of_org')
        all_orgs.add(org)

    all_profiles = sorted(all_profiles)
    all_orgs = sorted(all_orgs)


    locs = set()
    for intern in interns:
        loc = getattr(intern,'location')
        locs.add(loc)

    all_locs=sorted(locs)

    context = {
        'Faculties': interns[:3],
        'research_areas': all_profiles,
        'colleges': all_orgs,
        'locs':locs
    }
    
    return render(request, 'faculty/home.html', context)


