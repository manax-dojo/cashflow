from django.shortcuts import render


def HomeView(request):
    """
    """

    context = {}
    return render(request, 'homepage/home.html', context)
