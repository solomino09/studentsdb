# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
from django.template import RequestContext, loader
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

# Views for Groups
def groups_list(request):
    groups = (
        {'id': 1,
         'leader': u'Корост Андрей',
         'group_name': u'М- 314'},
        {'id': 2,
         'leader': u'Пупкин Вася',
         'group_name': u'МтМ - 22'},
        {'id': 3,
         'leader': u'Жмурик Федя',
         'group_name': u'КПТ - 08'}
    )
    return render(request, 'students/groups_list.html', {'groups': groups})
    #return HttpResponse('<h1>Groups Listing</h1>')
def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')
def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)
def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)

# Views for Journal
def journal_list(request):
    students = (
        {'id': 1,
         'first_name': u'Андрей',
         'last_name': u'Корост'},
        {'id': 2,
         'first_name': u'Вася',
         'last_name': u'Пупкин'},
        {'id': 3,
         'first_name': u'Федя',
         'last_name': u'Жмурик'}
    )
    #week = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
    return render(request, 'students/journal_list.html', {'students': students})
    #return HttpResponse('<h1>Journal Listing</h1>')

def journal_student(request, jid):
    return HttpResponse('<h1>Journal Listing Student %s</h1>' % jid)



#def test(request):
#    return render(request, 'students/students_list.html', {})
#    template = loader.get_template('demo.html')
#    context = RequestContext(request, {})
#    return HttpResponse(template.render(context))