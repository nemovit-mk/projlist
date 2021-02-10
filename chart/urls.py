from django.urls import path

from . import views

app_name = 'chart'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    path('pumps/', views.get_dots, name='get_dots'),
    path('jstest/', views.jsView.as_view(), name='jstest'),
]