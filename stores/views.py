from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from stores.models import *
from stores.serializers import *
from rest_framework.permissions import IsAuthenticated


class ListLocations(ListCreateAPIView):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]


class ListDepartment(ListCreateAPIView):

    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        locationid = self.kwargs.get("locationid")
        return Department.objects.filter(location=locationid)


class ListCategories(ListCreateAPIView):

    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.args)
        print(self.kwargs)
        locationid = self.kwargs.get("locationid")
        deparmentid = self.kwargs.get("departmentid")
        return Category.objects.filter(department__location=locationid, department=deparmentid)


class LocationManage(RetrieveUpdateDestroyAPIView):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]


class DepartmentManage(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]


class CategoryManage(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
