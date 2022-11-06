from django.urls import path
from .views import * 

urlpatterns = [
    path('addDivision' , DivisionApiView.as_view()),
    path('getDivisions' , AllDivisions.as_view())
]