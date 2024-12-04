from django.urls import path
from radmin.views import radmin, rdelete, redit

urlpatterns = [
    path('', radmin, name = 'radmin'),
    path('dels/<int:id>', rdelete, name = 'rdelete'),
    path('redit/<int:id>', redit, name = 'redit'),

    ]
