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
    # university = request.GET.get('org', None)

    loc = request.GET.get('loc',None)
    profile = request.GET.get('profile', None)
    mode = request.GET.get('mode',None)

    all_interns = Intern.objects.all()


    if loc and profile and mode:
        interns = all_interns.filter(location__icontains=unquote_plus(loc),
                                    profiles__icontains=unquote_plus(profile),
                                    work_mode__icontains=unquote_plus(mode))
    elif loc and profile:
        interns = all_interns.filter(location__icontains=unquote_plus(loc),
                                    profiles__icontains=unquote_plus(profile))
    elif loc and mode:
        interns = all_interns.filter(location__icontains=unquote_plus(loc),
                                    work_mode__icontains=unquote_plus(mode))
    elif profile and mode:
        interns = all_interns.filter(profiles__icontains=unquote_plus(profile),
                                    work_mode__icontains=unquote_plus(mode))
    elif loc:
        interns = all_interns.filter(location__icontains=unquote_plus(loc))
    elif profile:
        interns = all_interns.filter(profiles__icontains=unquote_plus(profile))
    elif mode:
        interns = all_interns.filter(work_mode__icontains=unquote_plus(mode))
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


    locs = set()
    for intern in all_interns:
        loc = getattr(intern,'location')
        loc = loc.capitalize()
        locs.add(loc)

    all_locs=sorted(locs)

    modes = set()
    for intern in all_interns:
        mode = getattr(intern,'work_mode')
        modes.add(mode)
    context = {
        'Faculties': interns[:3],
        'profiles': all_profiles,
        'colleges': all_orgs,
        'locs':all_locs,
        'modes':modes
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
        loc = loc.capitalize()
        locs.add(loc)
    all_locs=sorted(locs)

    modes = set()
    for intern in interns:
        mode = getattr(intern,'work_mode')
        modes.add(mode)
    context = {
        'Faculties': interns[:3],
        'profiles': all_profiles,
        'colleges': all_orgs,
        'locs':all_locs,
        'modes':modes
    }
    
    return render(request, 'faculty/home.html', context)


