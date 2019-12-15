from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('state_capitals.urls')),
    path('', include('breweries.urls')),
]
