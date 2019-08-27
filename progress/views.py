from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Q
from issues.models import Issue
from django.conf import settings
from datetime import datetime, timedelta, time
from django.utils import timezone

# Create your views here.
def progress_panel(request):
    """
    This view will return the progress_panel.html page.
    """
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    #today_start = datetime.combine(today, time())
    end_of_today = datetime.combine(tomorrow, time())
    
    start_of_week = datetime.combine(today - timedelta(7), time())
    #print(start_of_week)
    issues_solved_this_week = Issue.objects.filter(date_issue_solved__gte=timezone.make_aware(start_of_week)).filter(date_issue_solved__lt=timezone.make_aware(end_of_today)).count()
    #print(timezone.make_aware(start_of_week))
    start_of_month = datetime.combine(today - timedelta(28), time())
    issues_solved_this_month = Issue.objects.filter(date_issue_solved__gte=timezone.make_aware(start_of_month)).filter(date_issue_solved__lt=timezone.make_aware(end_of_today)).count()
    
    return render(request, "progress_panel.html", {'issues_solved_this_week': str(issues_solved_this_week), 'issues_solved_this_month': str(issues_solved_this_month)})


def get_issue_type_json(request):
    """
    This view will generate the json data required and outline 
    the type of chart to be used to display the data.
    """
    dataset = Issue.objects.values('issue_type').exclude(issue_type='').annotate(total=Count('issue_type')).order_by('issue_type')

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Issue Type'},
        'xAxis': {'type': "category"},
        'series': [{
            'name': 'Issue Type',
            'data': list(map(lambda row: {'name': [row['issue_type']], 'y': row['total']}, dataset))
        }]
    }
    return JsonResponse(chart)


def get_issue_status_json(request):
    """
    This view will generate the json data required and outline 
    the type of chart to be used to display the data.
    """
    dataset = Issue.objects \
        .values('status') \
        .exclude(status='') \
        .annotate(total=Count('status')) \
        .order_by('status')

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Issue Status'},
        'series': [{
            'name': 'Issue Status',
            'data': list(map(lambda row: {'name': [row['status']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)


def get_bug_upvotes_json(request):
    """
    This view will generate the json data required and outline 
    the type of chart to be used to display the data.
    """
    dataset = Issue.objects \
        .filter(issue_type='BUG') \
        .values('issue_upvotes', 'issue_name') \
        .exclude(issue_upvotes=0) \
        .order_by('issue_upvotes')

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Top Bug Upvotes'},
        'series': [{
            'name': 'Issue Upvotes',
            'data': list(map(lambda row: {'name': [row['issue_name']], 'y': row['issue_upvotes']}, dataset))
        }]
    }

    return JsonResponse(chart)
    
    
def get_feature_upvotes_json(request):
    """
    This view will generate the json data required and outline 
    the type of chart to be used to display the data.
    """
    dataset = Issue.objects \
    .filter(issue_type='FEATURE') \
    .values('issue_upvotes', 'issue_name') \
    .exclude(issue_upvotes=0) \
    .order_by('issue_upvotes')

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Top Feature Upvotes'},
        'series': [{
            'name': 'Issue Upvotes',
            'data': list(map(lambda row: {'name': [row['issue_name']], 'y': row['issue_upvotes']}, dataset))
        }]
    }

    return JsonResponse(chart)
    
    
''' Reference:
Author: Daly, J. (2019).
Title: "issue-tracker".
Version: Unknown.
Type: HTML, CSS, Python, Jinja, sqlite3, postgres.
Retrieved from: https://github.com/jordandaly/issue_tracker
'''