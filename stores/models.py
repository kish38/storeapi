from django.db import models


class Location(models.Model):
    location = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.location


class Department(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.department.name} - {self.category}"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.category.category} - {self.subcategory}"
