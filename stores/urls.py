from django.urls import path
from stores.views import ListLocations, ListDepartment, ListCategories
from stores.views import LocationManage, DepartmentManage, CategoryManage


urlpatterns = [
    path('location/', ListLocations.as_view()),
    path('location/<int:locationid>/department/', ListDepartment.as_view()),
    path('location/<int:locationid>/department/<int:departmentid>/category/', ListCategories.as_view()),

    path('location/<int:pk>/', LocationManage.as_view()),
    path('location/<int:locationid>/department/<int:pk>', DepartmentManage.as_view()),
    path('location/<int:locationid>/department/<int:departmentid>/category/<int:pk>', CategoryManage.as_view()),
]