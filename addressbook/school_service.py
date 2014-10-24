# coding=utf-8
from addressbook.models import School

__author__ = 'edwardotis'

'''
Service layer to organize school addressbook code better as use cases become more complex.
Prevents God and Big Ball of Mud anti-pattern in views.py
Allows for better unit testing and mocking.
'''

def get_schools_list(sort_by):
    schools = School.objects.all().order_by(sort_by)
    data = {}
    data['schools_list'] = schools
    return data