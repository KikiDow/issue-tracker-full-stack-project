from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from issues.models import Issue
from django.db.models import Count, Q
from .filters import IssueFilter

# Create your views here.
@login_required()
def search(request):
    f = IssueFilter(request.GET, queryset=Issue.objects.all())
    return render(request, 'search.html', {'filter': f})