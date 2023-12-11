from django.shortcuts import render



# Create your views here.
def landingFunction(request):
    context = {}
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

