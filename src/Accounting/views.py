from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', {})
    # return render(request, 'hack.html', {})
