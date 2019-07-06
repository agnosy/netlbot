import pprint

from newsapi import NewsApiClient
from .models.base import Session
from .models.article import Article
from .models.source import Source
from . import helpers

class Harvester:
    def __init__(self):
        self.api = NewsApiClient(api_key='27a7298d46f940ffbbb0f514a9b28496')
        self.pp = pprint.PrettyPrinter(indent=4)
        self.session = Session()

    def harvest(self, domains, sources, send_to_console, save_to_db):
        response = self.api.get_everything(sources=sources)
        print(
            f'retrieved [{response["totalResults"]}] articles'
            f' with status [{response["status"]}]'
        )

        articles = response["articles"]
        for article in articles:
            source = self.add_if_not_exists(
                self.session,
                article["source"]["id"],
                article["source"]["name"]
            )
            if send_to_console:
                self.pp.pprint(article)
            self.session.add(
                Article(
                    article["author"],
                    article["title"],
                    article["description"],
                    article["url"],
                    article["urlToImage"],
                    article["publishedAt"],
                    article["content"],
                    source,
                )
            )
        self.session.commit()

    def add_if_not_exists(self, session, text_id, name):
        source = session.query(Source).filter(Source.name.like(name)).first()
        if source is None:
            try:
                source = Source(text_id, name)
                session.add(source)
            except:
                return None
        return source

    def __del__(self):
        self.session.close()
