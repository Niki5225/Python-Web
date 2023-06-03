from django.urls import path, include

from exam1.web.views import index, add_album, album_details, album_edit, album_delete, profile_details, profile_delete, \
    add_profile

urlpatterns = (
    path('', index, name='index'),
    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', album_details, name='details album'),
        path('edit/<int:pk>/', album_edit, name='edit album'),
        path('delete/<int:pk>/', album_delete, name='delete album'),
    ])),
    path('profile/', include([
        path('details/', profile_details, name='details profile'),
        path('delete/', profile_delete, name='delete profile'),
    ])),
)
