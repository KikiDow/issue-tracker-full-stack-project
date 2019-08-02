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
    

@login_required()
def edit_issue(request, pk):
    """
    This view allows the contributor or staff member to edit a single issue.
    """
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    user = request.user
    
    if request.method == "POST":
        edit_issue_form = IssueForm(request.POST, request.FILES, instance=issue)
        if edit_issue_form.is_valid():

            edit_issue_form.instance.contributor = request.user
            if edit_issue_form.instance.issue_type == 'FEATURE':
                edit_issue_form.instance.price = 75
            else:
                edit_issue_form.instance.price = 0
            issue = edit_issue_form.save()
            messages.success(request, 'You have successfully made changes to this issue.')

            return redirect(view_issue, issue.pk)
    else:
        edit_issue_form = IssueForm(instance=issue)
        

    return render(request, "edit_issue.html", {'issue': issue, 'edit_issue_form': edit_issue_form})    
    

@login_required()
def upvote_issue(request, pk):
    """
    This view allows the user to upvote an issue of their choice.
    """
    issue = Issue.objects.get(pk=pk)
    issue.issue_upvotes += 1
    issue.save()
    messages.success(request, 'You have successfully upvoted this issue !!')
    return redirect('view_issue', pk)
    
@login_required()
def delete_issue(request, pk):
    """
    This view allows a staff member to delete a issue
    """
    issue_for_deletion = Issue.objects.get(pk=pk)
    issue_for_deletion.delete()
    messages.success(request, "You have successfully deleted this issue.")
    return redirect('index')