from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

"""Create your views here."""

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  # Delete the user account
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('home')  # Redirect to home or login page after deletion

    return render(request, 'delete_account.html')
