class Recommender:
    """
    Recommendation engine. Recommend articles stored in ES.
    """

    def get_users(self):
        available_users = (('user_0', 'No user selected'), ('user_1', 'User 1'), ('user_2', 'User 2'),)
        return available_users

    def recommend_articles(self, user_id):
        articles = []

        if user_id == 'user_1':
            articles = [
                {
                    'title': 'An article recommended for User 1',
                    'id': '3',
                    'url': 'https://omni.se/'
                },
                {
                    'title': 'Another article recommended for User 1',
                    'id': '4',
                    'url': 'https://omni.se/'
                }
            ]
        elif user_id == 'user_2':
            articles = [
                {
                    'title': 'Some article recommended for User 2',
                    'id': '5',
                    'url': 'https://omni.se/'
                }
            ]

        return articles

    def like_article(self, user_id, article_id):
        print(f'User {user_id} likes article {article_id}')
