# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

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

