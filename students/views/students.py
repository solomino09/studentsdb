# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# views for Students
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Андрей',
         'last_name': u'Корост',
         'ticket': 235,
         'image': 'img/1.jpeg'},
        {'id': 2,
         'first_name': u'Вася',
         'last_name': u'Пупкин',
         'ticket': 2123,
         'image': 'img/2.png'},
        {'id': 3,
         'first_name': u'Федя',
         'last_name': u'Жмурик',
         'ticket': 345,
         'image': 'img/3.jpg'}
    )
    return render(request, 'students/students_list.html', {'students': students})
def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

