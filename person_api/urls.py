from django.urls import path
from .views import PersonView, PersonRestrictedView, UserCreate

urlpatterns = [
    # path('', views.index, name='index'),
    path('people/', PersonView.as_view()),
    path('people/<str:username>', PersonView.as_view()),
    path('peoplerestricted/', PersonRestrictedView.as_view()),
    path("register", UserCreate.as_view())
]