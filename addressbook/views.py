# coding=utf-8
import logging

from django.http import Http404, HttpResponseBadRequest
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect

from addressbook import school_service
from addressbook.forms import SchoolForm
from addressbook.models import School
from mysite import db_util

logger = logging.getLogger(__name__)


class HipTemplateView(TemplateView):
    template_name = 'addressbook/index.html'

    def get(self, request, *args, **kwargs):
        response = super(HipTemplateView, self).get(request, *args, **kwargs)
        try:
            return response.render()
        except TemplateDoesNotExist:
            raise Http404()


def template_view(request, *args, **kwargs):
    return render(request, kwargs['template_name'])


def school_list(request, template_name='addressbook/schools.html'):
    if request.method == 'GET':
        # get sort_by param. Use - to sort descending
        sort_by = request.GET.get('sort_by', 'name')
        data = school_service.get_schools_list(sort_by)
        return render(request, template_name, data)


def create_school(request, template_name='addressbook/school_manage.html'):
    form = SchoolForm(request.POST or None)
    form.title = 'Add a School'
    if form.is_valid():
        school = form.save()
        return redirect('addressbook:school_detail', pk=school.school_id)
    return render(request, template_name, {'form': form})


def update_school(request, school_id, template_name='addressbook/school_manage.html'):
    school = get_object_or_404(School, pk=school_id)
    form = SchoolForm(request.POST or None, instance=school)
    form.title = 'Edit a School'
    if form.is_valid():
        school = form.save()
        db_util.log_and_clear_queries()
        return redirect('addressbook:school_detail', pk=school.school_id)
    return render(request, template_name, {'form': form})


def delete_school(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    if request.method == 'POST':
        school.delete()
        return redirect('addressbook:school_list')
    return HttpResponseBadRequest('Delete requires a POST request.')


def school_detail(request, pk, template_name='addressbook/school_detail.html'):
    school = get_object_or_404(School, pk=pk)
    return render(request, template_name, {'school': school})


