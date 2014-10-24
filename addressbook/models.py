# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse

__author__ = 'edwardotis'

class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, db_index=True)
    zipcode = models.IntegerField(max_length=5)
    email = models.EmailField()
    has_music_dept = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta(object):
        managed = True
        db_table = 'addressbook_school'

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('addressbook:school_detail', kwargs={'pk': str(self.school_id)})