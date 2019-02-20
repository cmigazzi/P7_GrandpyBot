import os

import googlemaps
from mediawiki import MediaWiki

from .parser.analyzer import QuestionAnalyzer


class RequestsManager():

    def __init__(self, question):
        self.question = QuestionAnalyzer(question)
        self.wiki = MediaWiki(lang="fr",
                              user_agent="GrandpyBot/OpenClassrooms")
        self.gmaps = googlemaps.Client(key=os.environ.get("G_API_KEY"))
        self.set_geocode_and_adress()
        self._articles = self.set_articles()

    def set_geocode_and_adress(self):
        keywords = ",".join(self.question.get_keywords())

        results = self.gmaps.geocode(keywords, region="fr")

        geocode = results[0]["geometry"]["location"]
        adress = results[0]["formatted_address"]
        self._geocode = geocode
        self._adress = adress

    def get_geocode(self):
        return self._geocode

    def get_adress(self):
        return self._adress

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
