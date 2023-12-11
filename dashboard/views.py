from .models import User, Tour
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate



# Create your views here.


def login_view(request):
  if request.method == "POST":
      email = request.POST.get('email')
      password = request.POST.get('password')
      keep_me_logged_in = request.POST.get('keep_me_logged_in')

      print(f"email: {email}")
      print(f"password: {password}")

      if not email:
          messages.error(request, 'Email is required.')
          return redirect('dashboard-login')

      if not User.objects.filter(email=email).exists():
          messages.error(request, 'No user with this email exists.')
          return redirect('dashboard-login')

      is_user = authenticate(request, email=email, password=password)
      print(f"is_user: {is_user}")
      if is_user:
          login(request, is_user)

      messages.success(request, "Message sent.")
      return redirect('dashboard-lpg-home')

  else:
      context = {}
      return render(request, 'auth/login.html', context)




@login_required
def tours(request):
    # Get the logged-in user (if any)
    logged_in_user = request.user
    # get tours
    tours = Tour.objects.all()

    context = {
        'user': logged_in_user,
        'tours':tours,
        # Add other data you want to pass to the template here
    }
    return render(request, 'dashboard/institutions.html', context)

@login_required
@csrf_protect
def tourStore(request):
    if request.method == "POST":

        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        venue = request.POST.get('venue')
        link = request.POST.get('link')

        # validation

        tour_record = Tour.objects.create(
            name=name,
            date=date,
            time=time,
            location=location,
            venue=venue,
            link=link,
        )

@login_required
def tourShow(request, tour_id):
    pass

@login_required
def tourUpdate(request, tour_id):
    pass

@login_required
def tourDelete(request, tour_id):
    pass

@login_required
def tourRestore(request, tour_id):
    pass






@login_required
def contactUs(request):
    pass

@login_required
def contactUsMarkViewed(request, contact_id):
    pass




@login_required
def users(request):
    pass

@login_required
def userStore(request):
    pass

@login_required
def userDelete(request, user_id):
    pass

