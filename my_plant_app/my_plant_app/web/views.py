from django.shortcuts import render, redirect

from my_plant_app.web.forms import CreateProfileForm, CreatePlantForm, PlantEditForm, PlantDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from my_plant_app.web.models import Profile, Plant


# Create your views here.

def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_plant():
    try:
        if Plant.objects.all():
            return Plant.objects.all()
    except Plant.DoesNotExist:
        return None


def index(request):
    if get_profile() is None:
        hide_nav_links = True
    else:
        hide_nav_links = False
    context = {
        'hide_nav_links': hide_nav_links,
    }

    return render(request, 'core/home-page.html', context)


def catalogue(request):
    if get_plant() is None:
        no_plants = True
        all_plants = None
    else:
        no_plants = False
        all_plants = Plant.objects.all()

    context = {
        'noPlants': no_plants,
        'allPlants': all_plants,

    }

    return render(request, 'core/catalogue.html', context)


def create_plant(request):
    if request.method == 'GET':
        form = CreatePlantForm()
    else:
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'plant/create-plant.html', context)


def details_plant(request, pk):
    context = {
        'plant': Plant.objects.get(pk=pk)
    }
    return render(request, 'plant/plant-details.html', context)


def edit_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'plant/edit-plant.html', context)


def delete_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'plant/delete-plant.html', context)


def profile_details(request):
    if get_profile() is None:
        is_profile = False
        profile = None
    else:
        is_profile = True
        profile = Profile.objects.get()

    plants_count = Plant.objects.count()

    context = {
        'thereIsProfile': is_profile,
        'profile': profile,
        'plantsCount': plants_count
    }
    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = PlantEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profile/delete-profile.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)
