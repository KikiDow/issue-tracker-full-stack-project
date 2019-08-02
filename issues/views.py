from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Issue, Comment
from .forms import IssueForm, CommentForm

# Create your views here.
def landing_page(request):
    """
    Create a view that will render the landing page to the user.
    """
    all_issues = Issue.objects.all().order_by('-date_issue_created')
    
    return render(request, "landing_page.html", {'issues': all_issues})
    
    
@login_required()
def create_issue(request):
    """
    Implement the view that allows a user to report a new bug or suggest a new feature.
    """
    if request.method == "POST":
        create_issue_form = IssueForm(request.POST, request.FILES)
        if create_issue_form.is_valid():
            
            create_issue_form.instance.contributor = request.user
            if create_issue_form.instance.issue_type == 'FEATURE':
                create_issue_form.instance.price = 75
            else:
                create_issue_form.instance.price = 0
            issue = create_issue_form.save()
            messages.success(request, 'You have successfully contributed a new issue to the site.')
            
            return redirect(view_issue, issue.pk)
    else:
        create_issue_form = IssueForm()
    return render(request, 'create_issue_form.html', {'create_issue_form': create_issue_form})
    
    
@login_required()
def view_issue(request, pk):
    """
    This view allows the user to view a single issue.
    """
    issue = get_object_or_404(Issue, pk=pk)
    issue.save()

    return render(request, "view_issue.html", {'issue': issue})