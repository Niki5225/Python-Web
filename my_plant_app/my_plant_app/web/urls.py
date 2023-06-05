from django.urls import path, include

from my_plant_app.web.views import index, edit_plant, edit_profile, delete_plant, details_plant, delete_profile, \
    profile_details, create_profile, create_plant, catalogue

urlpatterns = (
    path('', index, name='index'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
        path('details/', profile_details, name='details profile'),
    ])),
    path('plant/', include([
        path('create/', create_plant, name='create plant'),
        path('details/<int:pk>/', details_plant, name='details plant'),
        path('edit/<int:pk>/', edit_plant, name='edit plant'),
        path('delete/<int:pk>/', delete_plant, name='delete plant'),
    ])),
    path('catalogue/', catalogue, name='catalogue'),
)
