import os

import googlemaps
from mediawiki import MediaWiki

from .parser.analyzer import QuestionAnalyzer


class RequestsManager():

    def __init__(self, question):
        self.question = QuestionAnalyzer(question)
        self._geocode = self.set_geocode()
        self._articles = self.set_articles()

    def set_geocode(self):
        api_key = os.environ.get("G_API_KEY")
        gmaps = googlemaps.Client(key=api_key)
        keywords = ",".join(self.question.get_keywords())

        results = gmaps.geocode(keywords, region="fr")

        geocode = results[0]["geometry"]["location"]

        return geocode

    def set_articles(self):
        params = {"lang": "fr", "user-agent": "GrandpyBot/OpenClassrooms"}
        wikipedia = MediaWiki(**params)
        latitude = self._geocode["lat"]
        longitude = self._geocode["lng"]
        articles = wikipedia.geosearch(latitude=latitude, longitude=longitude)

        return articles
