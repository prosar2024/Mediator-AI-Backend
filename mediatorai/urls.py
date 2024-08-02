from django.urls import path, include

urlpatterns = [
    path('mediatorai/', include("app.urls")),
]
