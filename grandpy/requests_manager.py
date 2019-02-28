"""Contains the manager of the requests."""

import os

import googlemaps
from mediawiki import MediaWiki

from .parser.analyzer import QuestionAnalyzer
from .parser.exceptions import ZeroResultException


class RequestsManager():
    """Represent the manager of requests.

    It calls the annalyzer, get the keywords and call API's to get results.

    Raises:
        ZeroResultException -- No result in geocoding API call.

    Methods:
        set_geocode_and_adress() -- Call gmaps API to get geocode and adress.
        get_geocode() -- Return geocodes.
        get_adress() -- Return adress.
        set_articles() -- Call Wikimedia API to get articles from geocodes.
        get_articles() -- Return articles titles.
        get_summary() -- Get the summary of the first article.

    """

    def __init__(self, question):
        """Construct the RequestManager object.

        Arguments:
            question {str} -- user question.
        """
        self.question = QuestionAnalyzer(question)
        self.wiki = MediaWiki(lang="fr",
                              user_agent="GrandpyBot/OpenClassrooms")
        self.gmaps = googlemaps.Client(key=os.environ.get("G_API_KEY"))
        self.set_geocode_and_adress()
        self._articles = self.set_articles()

    def set_geocode_and_adress(self):
        """Call gmaps API to get geocode and adress.

        Raises:
            ZeroResultException -- No result in geocoding API call.

        """
        keywords = ",".join(self.question.get_keywords())

        results = self.gmaps.geocode(keywords, region="fr")

        if results == []:
            raise ZeroResultException

        geocode = results[0]["geometry"]["location"]
        adress = results[0]["formatted_address"]
        self._geocode = geocode
        self._adress = adress

    def get_geocode(self):
        """Return geocodes."""
        return self._geocode

    def get_adress(self):
        """Return adress."""
        return self._adress

    def set_articles(self):
        """Call Wikimedia API to get articles from geocodes.

        Returns:
            [list] -- articles titles

        """
        latitude = self.get_geocode()["lat"]
        longitude = self.get_geocode()["lng"]
        articles = self.wiki.geosearch(latitude=latitude, longitude=longitude)

        return articles

    def get_articles(self):
        """Return articles titles."""
        return self._articles

    def get_summary(self):
        """Get the summary of the first article.

        Returns:
            [str] -- summary of the article

        """
        title = self.get_articles()[0]
        summary = self.wiki.summary(title)
        return summary
