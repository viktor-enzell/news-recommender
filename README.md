# News Recommender
Group project in **DD2476 Search Engines and Information Retrieval Systems** at **KTH** in 2021.

A personalized news recommendation system built in Python with [Django](https://www.djangoproject.com/), [Elasticsearch](https://www.elastic.co/), [Scrapy](https://scrapy.org/) and [Doc2Vec](https://radimrehurek.com/gensim/models/doc2vec.html). 
News articles are scraped from [bbc.com/news](https://www.bbc.com/news) and stored in Elasticsearch. 
A Doc2Vec model is then trained on these articles and the articles are updated to include a vector representation produced by the model. 
When interacting with the system, the user chooses from a list of predefined user profiles and based on articles that the user likes or dislikes, the user profile is adapted to represent the user's preferences.

## Getting Started
The recommended Python version for this project is Python 3.8 or later.
It is generally recommended to start a new Virtualenv before installing the project requirements.

For testing the system, you can load a set of articles from file and use our pretrained Doc2Vec model.
To do this, just follow the instructions below. 
If you want to crawl new articles and train the model from scratch, 
then skip the step where you populate Elasticsearch with news articles and instead follow the optional instructions below.

Follow the instructions on [elastic.co](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) to install Elasticsearch.

Install the project requirements.
```
pip install -r requirements.txt
```

Unzip the pretrained Doc2Vec model.
```
unzip d2v_120k_pre.zip
```

Populate Elasticsearch with news articles by first creating an index and then loading the already crawled articles into the index.
```
elasticdump --input=./es/scrapy-1-mapping.json --output=http://localhost:9200/scrapy-1 --type=mapping
elasticdump --input=./es/scrapy-1.json --output=http://localhost:9200/scrapy-1 --type=data
```

Initialize user profiles.
```
python manage.py create_users
```

Start the Django server.
```
python manage.py runserver
```

You should now be able to interact with the system at http://127.0.0.1:8000/.

### Optional: Crawl new news articles and train a Doc2Vec model from scratch
Crawl BBC for news articles. 
This can take a while, depending on the depth you set in **scrapysettings.py**.
```
python manage.py crawl
```

Train the Doc2Vec model on the imported articles:
```
python manage.py train_model
```

Associate each article with a Doc2Vec vector representation:
```
python manage.py encode
```

## Project Structure
The project is roughly structured as follows. 
```
es/ <- pre-crawled news articles
project/ <- project settings
recommender/
    management/
        commands/ <- commands for crawling and model training etc.
    templates/ <- html templates
    views.py <- views
    recommender.py <- recommendation engine
    ...
d2v_120k_pre.zip <- zipped pretrained Doc2Vec model
scrapysettings.py <- where you set depth for scraping
...
```
