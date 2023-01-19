from django.urls import path
from .views import PersonView

urlpatterns = [
    # path('', views.index, name='index'),
    path('people/', PersonView.as_view()),
    path('people/<str:username>', PersonView.as_view())
]