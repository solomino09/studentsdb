# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# views for Students
def students_list(request):
    return render(request, 'students/students_list.html', {})
def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups
def groups(request):
    return HttpResponse('<h1>Groups Listing</h1>')
def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')
def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)
def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)

# Views for Journal
def journal_list(request):
    return HttpResponse('<h1>Journal Listing</h1>')
def journal_student(request, jid):
    return HttpResponse('<h1>Journal Listing Student %s</h1>' % jid)



#def test(request):
#    return render(request, 'students/students_list.html', {})
#    template = loader.get_template('demo.html')
#    context = RequestContext(request, {})
#    return HttpResponse(template.render(context))