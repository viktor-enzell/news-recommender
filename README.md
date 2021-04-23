# News Recommender

## Getting Started
The recommended Python version for this project is Python 3.8. 
[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) is a helpful tool for handling different Python versions together with different Virtualenvs. 
It is recommended to start a new Virtualenv before installing the project requirements.

Install requirements:
```
pip install -r requirements.txt
```

Start the Django server: 
```
python manage.py runserver
```

### Elasticsearch
In order to run the project, articles have to be crawled and users-profiles need to be defined. 
Both articles and user-profiles are stored in Elasticsearch and are imported using Django commands.

Import articles from BBC:
```
python manage.py crawl
```

Initialize user-profiles:
```
python manage.py create_users
```


## Project Structure
The project is roughly structured as follows. 
```
project/ <- project settings
recommender/
    management/
        commands/
            crawl.py <- web crawler
    templates/ <- UI templates
    views.py <- views
    recommender.py <- recommendation engine
    ...
...
```
The web crawler operates asynchronously and crawls the web for news articles and stores the articles in Elasticsearch.

The UI presents the user with a list of user-profiles to choose from. 
Based on the chosen user-profile (and maybe a search query) the user is presented with a list of recommended articles and the user has the option to like articles.

The views mediate requests between the UI and the recommendation engine.

The recommendation engine takes a user-id (and maybe a search query) as the input and returns a list of recommended articles based on the articles in Elasticsearch and the recommendation algorithm. 
When a user likes an article, the recommendation engine incorporates the feedback in the user-profile and updates the recommendation. 
