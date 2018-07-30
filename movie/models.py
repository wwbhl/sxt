# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Area(models.Model):
    areaid = models.IntegerField(db_column='areaID')
    area = models.CharField(max_length=20)
    fatherid = models.IntegerField(db_column='fatherID')

    class Meta:
        managed = False
        db_table = 'area'
class Movie(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(unique=True,max_length=100)
    mdesc = models.TextField(blank=True,null=True)
    mimg = models.CharField(max_length=120)
    mlink = models.CharField(max_length=200)
    def __unicode__(self):
        return u'%s'%self.mname.strip()
    class Meta:
        managed = False
        db_table = 'movie'

class Province(models.Model):
    provinceid = models.IntegerField(db_column='provinceID')
    provice = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'province'


class StudentsClassroom(models.Model):
    cname = models.CharField(unique=True,max_length=20)

    class Meta:
        managed = False
        db_table = 'students_classroom'

class StudentsStudent(models.Model):
    sname = models.CharField(max_length=10)
    ssex = models.IntegerField()
    sdate = models.DateField()
    croom = models.ForeignKey(StudentsClassroom,models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'students_student'

class SxtLove(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'sxt_love'

class SxtUser(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sxt_user'

class User(models.Model):
    name = models.CharField(max_length=20)
    birthday = models.DateField()

    def __unicode__(self):
        return u'%s'%self.name
