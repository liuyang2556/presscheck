from django.urls import path
from . import views
from haystack.views import SearchView

# start with blog
urlpatterns = [
    # http://localhost:8000/blog/
    path('', views.checksheet_list, name="checksheet_list"),
    # path('bl/', views.blchecksheet_list, name="blchecksheet_list"),
    path('<int:checksheet_pk>', views.checksheet_page, name="checksheet_page"),
    path('car_type/<int:car_type_pk>', views.cars_with_type, name="cars_with_type"),
    path('updatesheet_data>', views.updatesheet_data, name="updatesheet_data"),
    path('updatesheet/<int:updatesheet_pk>', views.updatesheet_page, name="updatesheet_page"),
    path('updatesheet', views.updatesheet_list, name="updatesheet_list"),
    path('tendencychart', views.tendencychart_list, name="tendencychart_list"),
    path('tendencychart/<int:checksheet_pk>', views.tendencychart_page, name="tendencychart_page"),
    path('search2/', views.search2, name="search2"),
    path('search3/', views.search3, name="search3"),
]
