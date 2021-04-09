from django.shortcuts import render


def index(request):
    articles = [
        {
            'title': 'Article 1',
            'url': 'https://omni.se/'
        },
        {
            'title': 'Article 2',
            'url': 'https://omni.se/'
        }
    ]
    context = {'articles': articles}
    return render(request, 'index.html', context)
