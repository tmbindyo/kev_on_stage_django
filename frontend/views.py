from datetime import datetime
from django.db.models import Q
from django.shortcuts import render
from dashboard.models import Tour



# Create your views here.
def landingFunction(request):
    now = datetime.now()
    # get_tours = Tour.objects.all()
    # print(f"get_tours:{get_tours}")


    # Filter tours where is_sold_out is False and the date is greater than or equal to today
    tours = Tour.objects.filter(is_sold_out=False, date__gte=now.date(), time__gte=now.time())

    # print(f"tours:{tours}")
    context = {
        "tours":tours,
    }
    return render(request, 'index.html', context)


def landingStudioSpaceFunction(request):
    context = {}
    return render(request, 'index.html', context)


def landingListenFunction(request):
    context = {}
    return render(request, 'index.html', context)


def contactUs(request):
    context = {}
    return render(request, 'index.html', context)

