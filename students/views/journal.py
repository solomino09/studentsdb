# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Views for Journal
def journal_list(request):
    leaders = (
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
    week = (
        {'day_of_week': u'Вс',
         'day': 1},
        {'day_of_week': u'Пн',
         'day': 2},
        {'day_of_week': u'Вт',
         'day': 3},
        {'day_of_week': u'Ср',
         'day': 4},
        {'day_of_week': u'Чт',
         'day': 5},
        {'day_of_week': u'Пт',
         'day': 6},
        {'day_of_week': u'Сб',
         'day': 7},
        {'day_of_week': u'Вс',
         'day': 8},
        {'day_of_week': u'Пн',
         'day': 9},
        {'day_of_week': u'Вт',
         'day': 10},
        {'day_of_week': u'Ср',
         'day': 11},
        {'day_of_week': u'Чт',
         'day': 12},
        {'day_of_week': u'Пт',
         'day': 13},
        {'day_of_week': u'Сб',
         'day': 14},
        {'day_of_week': u'Вс',
         'day': 15},
        {'day_of_week': u'Пн',
         'day': 16},
        {'day_of_week': u'Вт',
         'day': 17},
        {'day_of_week': u'Ср',
         'day': 18},
        {'day_of_week': u'Чт',
         'day': 19},
        {'day_of_week': u'Пт',
         'day': 20},
        {'day_of_week': u'Сб',
         'day': 21},
        {'day_of_week': u'Вс',
         'day': 22},
        {'day_of_week': u'Пн',
         'day': 23},
        {'day_of_week': u'Вт',
         'day': 24},
        {'day_of_week': u'Ср',
         'day': 25},
        {'day_of_week': u'Чт',
         'day': 26},
        {'day_of_week': u'Пт',
         'day': 27},
        {'day_of_week': u'Сб',
         'day': 28},
        {'day_of_week': u'Сб',
         'day': 29},
        {'day_of_week': u'Сб',
         'day': 30},
        {'day_of_week': u'Сб',
         'day': 31},
    )
    return render(request, 'students/journal_list.html', {'leaders': leaders, 'week': week})
def journal_student(request, jid):
    return HttpResponse('<h1>Journal Listing Student %s</h1>' % jid)
