from django.shortcuts import render, redirect

from exam1.web.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, ProfileDeleteForm
from exam1.web.models import Profile, Album


# Create your views here.

def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form,
               'hide_nav_links': True,}

    return render(request, 'core/home-no-profile.html', context)


def index(request):
    if get_profile() is None:
        return add_profile(request)

    context = {
        'albums': Album.objects.all(),
    }

    return render(request, 'core/home-with-profile.html', context)


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'album/add-album.html', context)


def album_details(request, pk):
    context = {
        'album': Album.objects.get(pk=pk)
    }
    return render(request, 'album/album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'album/edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'album/delete-album.html', context)


def profile_details(request):
    context = {
        'profile': Profile.objects.get(),
        'allalbums': Album.objects.count()
    }
    return render(request, 'profile/profile-details.html', context)


def profile_delete(request):
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
    return render(request, 'profile/profile-delete.html', context)
