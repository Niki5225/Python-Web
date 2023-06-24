from django.shortcuts import render, redirect

from frutipedia_app.web.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from frutipedia_app.web.models import Profile, Fruit


# Create your views here.

def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_fruits():
    try:
        return Fruit.objects.all()
    except Fruit.DoesNotExist:
        return None


def index(request):
    if get_profile() is None:
        hide_nav_links = True
    else:
        hide_nav_links = False
    context = {
        'hide_nav_links': hide_nav_links,
    }

    return render(request, 'core/index.html', context)


def dashboard(request):
    if get_fruits() is None:
        fruits = None
    else:
        fruits = get_fruits()

    context = {
        'fruits': fruits,
    }

    return render(request, 'core/dashboard.html', context)


def profile_create_page(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def profile_edit_page(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete_page(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'profile/delete-profile.html', context)


def profile_details_page(request):
    context = {
        'profile': get_profile(),
        'posts': Fruit.objects.count()
    }
    return render(request, 'profile/details-profile.html', context)


def fruit_create_page(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }
    return render(request, 'fruit/create-fruit.html', context)


def fruit_delete_page(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    if request.method == "GET":
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'fruit/delete-fruit.html', context)


def fruit_details_page(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    context = {
        'fruit': fruit,
    }
    return render(request, 'fruit/details-fruit.html', context)


def fruit_edit_page(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    if request.method == "GET":
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'fruit/edit-fruit.html', context)
