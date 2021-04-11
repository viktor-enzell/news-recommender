from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UserForm
from .recommender import Recommender

# Not sure if having recommender as a separate class is the "Django way of doing things".
# Not sure if this is the proper place to instantiate the recommender either.
recommender = Recommender()


def index(request):
    """
    Handling all GET and POST requests.
    """
    available_users = recommender.get_users()

    if request.method == 'GET':
        user = request.session.get('user', None)

        if user and user != 'user_0':
            # If user is already selected, return recommended articles
            articles = recommender.recommend_articles(user)
            form = UserForm(initial_user=user, available_users=available_users)
        else:
            # If user is not selected, return a set of random articles.
            # Maybe return no articles before user is selected instead?.
            articles = recommender.get_random_articles()
            form = UserForm(available_users=available_users)

        context = {
            'form': form,
            'articles': articles
        }
        return render(request, 'index.html', context)

    if request.method == 'POST':
        if request.POST.get('select_user', False):
            # Handle post request for selecting user
            form = UserForm(request.POST, available_users=available_users)
            if form.is_valid():
                data = form.cleaned_data
                if data.get('user'):
                    request.session['user'] = data.get('user')

        elif request.POST.get('like_article', False):
            # Handle post request for user liking article
            user = request.session['user']
            article = request.POST.get('like_article')
            recommender.like_article(user, article)

        # Redirect back to / so that a GET request is sent and the articles are updated
        return HttpResponseRedirect('/')
