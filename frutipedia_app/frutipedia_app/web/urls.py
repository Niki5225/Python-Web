from django.urls import path, include

from frutipedia_app.web.views import index, dashboard, profile_create_page, fruit_create_page, profile_delete_page, \
    fruit_delete_page, fruit_details_page, profile_details_page, profile_edit_page, fruit_edit_page

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', fruit_create_page, name='create fruit'),
    path('<int:pk>/', include([
        path('details/', fruit_details_page, name='details fruit'),
        path('delete/', fruit_delete_page, name='delete fruit'),
        path('edit/', fruit_edit_page, name='edit fruit'),
    ])),
    path('profile/', include([
        path('create/', profile_create_page, name='create profile'),
        path('delete/', profile_delete_page, name='delete profile'),
        path('edit/', profile_edit_page, name='edit profile'),
        path('details/', profile_details_page, name='details profile'),
    ])),
)

