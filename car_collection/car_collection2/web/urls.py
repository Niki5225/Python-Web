from django.urls import path, include

from car_collection2.web.views import index, catalogue, create_car, create_profile, delete_car, details_profile, \
    details_car, delete_profile, edit_car, edit_profile

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
        path('details/', details_profile, name='profile details'),
    ])),
    path('car/', include([
        path('create/', create_car, name='create car'),
        path('<int:pk>/', include([
            path('details/', details_car, name='car details'),
            path('edit/', edit_car, name='edit car'),
            path('delete/', delete_car, name='delete car'),
        ])),
    ])),
)
