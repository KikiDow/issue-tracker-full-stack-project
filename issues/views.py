from django.shortcuts import render, redirect, HttpResponseRedirect

# Create your views here.
def landing_page(request):
    """
    Create a view that will render the landing page to the user.
    """
    return render(request, "landing_page.html")