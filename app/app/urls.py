from django.urls import path, include

urlpatterns = [
    path('', include('breweries.urls')),
    path('', include('state_capitals.urls')),
]
