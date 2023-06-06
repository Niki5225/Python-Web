from django.shortcuts import render, redirect

from car_collection2.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from car_collection2.web.models import Profile, Car


# Create your views here.

def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_cars():
    try:
        return Car.objects.all()
    except Car.DoesNotExist:
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


def catalogue(request):
    if get_cars() is None:
        all_cars = False
        cars_count = None
    else:
        all_cars = Car.objects.all()
        cars_count = Car.objects.count()

    context = {
        'cars': all_cars,
        'carsCount': cars_count,
    }
    return render(request, 'core/catalogue.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-create.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/profile-edit.html', context)


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
        'profile': profile,
        'form': form
    }

    return render(request, 'profile/profile-delete.html', context)


def details_profile(request):
    cars = Car.objects.all()
    price = 0
    for car in cars:
        price += car.price

    context = {
        'profile': Profile.objects.get(),
        'totalPrice': price,
    }
    return render(request, 'profile/profile-details.html', context)


def create_car(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'car/car-create.html', context)


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car/car-delete.html', context)


def details_car(request, pk):
    car = Car.objects.get(pk=pk)

    context = {
        'car': car,
    }

    return render(request, 'car/car-details.html', context)
