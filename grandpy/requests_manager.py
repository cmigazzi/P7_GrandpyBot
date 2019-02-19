import os

import googlemaps
from mediawiki import MediaWiki

from .parser.analyzer import QuestionAnalyzer


class RequestsManager():

    def __init__(self, question):
        self.question = QuestionAnalyzer(question)
        self.wiki = MediaWiki(lang="fr", user_agent="GrandpyBot/OpenClassrooms")
        self._geocode = self.set_geocode()
        self._articles = self.set_articles()

    def set_geocode(self):
        api_key = os.environ.get("G_API_KEY")
        gmaps = googlemaps.Client(key=api_key)
        keywords = ",".join(self.question.get_keywords())

        results = gmaps.geocode(keywords, region="fr")

        geocode = results[0]["geometry"]["location"]

        return geocode

    def get_geocode(self):
        return self._geocode

    def set_articles(self):
        latitude = self.get_geocode()["lat"]
        longitude = self.get_geocode()["lng"]
        articles = self.wiki.geosearch(latitude=latitude, longitude=longitude)

        return articles

    def get_articles(self):
        return self._articles

    def get_summary(self):
        title = self.get_articles()[0]
        summary = self.wiki.summary(title)
        return summary
