# coding=utf-8
from django.forms import ModelForm

from addressbook.models import School


__author__ = 'edwardotis'


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['name', 'zipcode', 'email', 'has_music_dept', 'school_id']
