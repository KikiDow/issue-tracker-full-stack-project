from issues.models import Issue
import django_filters

class IssueFilter(django_filters.FilterSet):
    class Meta:
        model = Issue
        fields = ['issue_name', 'contributor', 'is_issue_solved', 'tag', 'status']