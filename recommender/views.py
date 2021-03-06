from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UserForm, SearchForm
from .recommender import Recommender

recommender = Recommender()


def index(request):
    """
    Handling all GET and POST requests.
    """
    available_users = recommender.get_users()

    if request.method == 'GET':
        user = request.session.get('user', None)

        if user and user != 'no_user_selected':
            # If user is already selected, return search form
            user_form = UserForm(initial_user=user, available_users=available_users)

            if request.GET.get('query', False):
                # If user has entered a search query, return corresponding articles
                search_form = SearchForm(request.GET)
                if search_form.is_valid():
                    query = search_form.cleaned_data.get('query', False)
                    if query:
                        request.session['query'] = query
                        articles = recommender.recommend_articles(user, query)
                        liked_articles, disliked_articles = recommender.get_reviewed_articles(user)
                        context = {
                            'user_form': user_form,
                            'search_form': search_form,
                            'articles': articles,
                            'liked_articles': liked_articles,
                            'disliked_articles': disliked_articles
                        }
                        return render(request, 'index.html', context)

            # If user has not entered a search query, return an empty search form
            search_form = SearchForm()
            context = {
                'user_form': user_form,
                'search_form': search_form
            }
            return render(request, 'index.html', context)
        else:
            # If user is not selected, return no search form and no articles
            user_form = UserForm(available_users=available_users)
            context = {
                'user_form': user_form,
                'articles': []
            }
            return render(request, 'index.html', context)

    if request.method == 'POST':
        if request.POST.get('user', False):
            # Handle post request for selecting user
            user_form = UserForm(request.POST, available_users=available_users)
            if user_form.is_valid():
                data = user_form.cleaned_data
                if data.get('user'):
                    request.session['user'] = data.get('user')
            return HttpResponseRedirect('/')

        user = request.session['user']
        if request.POST.get('like_article', False):
            # Handle post request for user liking article
            article = request.POST.get('like_article')
            recommender.like_article(user, article)

        elif request.POST.get('dislike_article', False):
            # Handle post request for user disliking article
            article = request.POST.get('dislike_article')
            recommender.dislike_article(user, article)

        query = request.session['query']
        return HttpResponseRedirect(f'/?query={query}') if query else HttpResponseRedirect('/')
