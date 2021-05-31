from django.db import models

# Create your models here.

class Post(models.Model):
    blog_title = models.CharField(max_length =  30)
    blog_date = models.DateTimeField()
    blog_image = models.ImageField(upload_to = 'blog_images/')
    blog_text = models.TextField(max_length = 300)


    def __str__(self):
        return self.blog_title

class Test(models.Model):
    test_title = models.CharField(max_length = 50)

    def __str__(self):
        return self.test_title


class Member(models.Model):
    member_ID = models.IntegerField()
    member_FIO = models.CharField(max_length = 50)
    member_sex = models.CharField(max_length = 1)
    member_birthdate = models.DateField()
    member_age = models.IntegerField()
    member_lastRoute_id = models.IntegerField()
    member_routeCount = models.IntegerField()
    member_group_id = models.IntegerField()
    member_login = models.CharField(max_length = 50)
    member_password = models.CharField(max_length = 50)
    member_status = models.IntegerField()
    member_cathegory = models.IntegerField()

class Coach(models.Model):
    coach_ID = models.IntegerField()
    coach_FIO = models.CharField(max_length = 50)
    coach_age = models.CharField(max_length = 50)
    coach_competitionID = models.IntegerField()
    coach_salary = models.IntegerField()
    coach_specialization = models.CharField(max_length = 50)
    coach_works = models.IntegerField()
    coach_sectionId = models.IntegerField()
    coach_routeCount = models.IntegerField()
    coach_login = models.CharField(max_length = 50)
    coach_password = models.CharField(max_length = 50)

class Admin(models.Model):
    admin_ID = models.IntegerField()
    admin_FIO = models.CharField(max_length = 50)
    admin_birthday = models.DateField()
    admin_age = models.IntegerField()
    admin_salary = models.IntegerField()
    admin_startDate = models.DateField()
    admin_sectionID = models.IntegerField()
    admin_login = models.CharField(max_length = 50)
    admin_password = models.CharField(max_length = 50)

class Section(models.Model):
    section_ID = models.IntegerField()
    section_name = models.CharField(max_length = 50)
    section_materialList = models.CharField(max_length = 50)
    section_routeId = models.IntegerField()

class Route(models.Model):
    route_ID = models.IntegerField()
    route_coachID = models.IntegerField()
    route_sectionID = models.IntegerField()
    route_startDate = models.DateField()
    route_endDate = models.DateField()
    route_cathegory = models.IntegerField()
    route_length = models.IntegerField()
    route_equipment = models.CharField(max_length = 50)
    route_material = models.CharField(max_length = 50)
    route_products = models.CharField(max_length = 50)

class Group(models.Model):
    group_ID = models.IntegerField()
    group_coachID = models.IntegerField()
    group_startDate = models.DateField()
    group_endDate = models.DateField()
    group_cathegory = models.IntegerField()

class Storage(models.Model):
    storage_ID = models.IntegerField()
    storage_equipment = models.CharField(max_length = 50)
    storage_material = models.CharField(max_length = 50)
    storage_products = models.CharField(max_length = 50)
    storage_routeID = models.IntegerField()
    storage_adminID = models.IntegerField()
