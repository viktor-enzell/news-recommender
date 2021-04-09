from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponseRedirect


def index(request):
    """
    TODO:
        instantiate recommender somewhere
        get users from recommender
        get random news from recommender
        send users and news to UI
        retrieve selected user from UI
        keep track of a mapping between session and user
        send updated news to UI
        retrieve feedback from UI and pass to recommender
        send updated news to UI
    """
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

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            if data.get('user'):
                request.session['user'] = data.get('user')
                return HttpResponseRedirect('/')

    if request.session.get('user', False):
        form = UserForm(initial_user=request.session.get('user', False))
    else:
        form = UserForm()

    context = {
        'form': form,
        'articles': articles
    }
    return render(request, 'index.html', context)
