import pytest
import googlemaps
from mediawiki import MediaWiki

from grandpy import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app({
        'TESTING': True,
    })

    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def questions():
    return {
        0: {"question": "Est-ce que tu connais l'adresse d'openclassrooms ?",
            "words": ["est", "ce", "que", "tu", "connais", "l", "adresse",
                      "d", "openclassrooms"],
            "keywords": ["openclassrooms"]
            },
        1: {"question": "Connais-tu l'adresse d'Openclassrooms ?",
            "words": ["connais", "tu", "l", "adresse", "d", "openclassrooms"],
            "keywords": ["openclassrooms"]
            },
        2: {"question": "tu connais l'adresse d'Openclassrooms ?",
            "words": ["tu", "connais", "l", "adresse", "d", "openclassrooms"],
            "keywords": ["openclassrooms"]
            },
        3: {"question": "Ou se trouve l'arc de triomphe ?",
            "words": ["ou", "se", "trouve", "l", "arc", "de", "triomphe"],
            "keywords": ["arc", "triomphe"]
            },
        4: {"question": "Quelle est l'adresse de l'arc de triomphe ?",
            "words": ["quelle", "est", "l", "adresse", "de", "l", "arc",
                      "de", "triomphe"],
            "keywords": ["arc", "triomphe"]
            },
        5: {"question": "Le stade de France, tu connais ?",
            "words": ["le", "stade", "de", "france", "tu", "connais"],
            "keywords": ["stade", "france"]
            },
        6: {"question": ("Connaissez-vous l'adresse du Monoprix "
                         "de Villeurbanne ?"),
            "words": ["connaissez", "vous", "l", "adresse", "du",
                      "monoprix", "de", "villeurbanne"],
            "keywords": ["monoprix", "villeurbanne"]
            },
        7: {"question": "Peux-tu me dire où se trouve la gare Saint-Paul ?",
            "words": ["peux", "tu", "me", "dire", "où", "se", "trouve", "la",
                      "gare", "saint", "paul"],
            "keywords": ["gare", "saint", "paul"]
            },
        8: {"question": ("Salut GrandPy ! Est-ce que tu connais l'adresse "
                         "d'OpenClassrooms ?"),
            "words": ["est", "ce", "que", "tu", "connais",
                      "l", "adresse", "d", "openclassrooms"],
            "keywords": ["openclassrooms"]
            },
        9: {"question": ("Hey Grandpy! La place Bellecour, "
                         "ca te dit quelque chose ?"),
            "words": ["la", "place", "bellecour", "ca", 
                      "te", "dit", "quelque", "chose"],
            "keywords": ["place", "bellecour"]
            },
        10: {"question": "Hey, ou se trouve la place Bellecour ?",
             "words": ["hey", "ou", "se", "trouve",
                       "la", "place", "bellecour"],
             "keywords": ["place", "bellecour"]
             }

    }


@pytest.fixture(autouse=True)
def google_api_call(monkeypatch):
    def mock_init(*args, **kwargs):
        pass
    monkeypatch.setattr(googlemaps.Client, "__init__", mock_init)

    def mock_geocode(*args, **kwargs):
        return [{"geometry":
                {"location": {'lat': 48.9244592, 'lng': 2.3601645}},
                "formatted_address": "Stade de France, 93200 Saint-Denis"
                 }]
    monkeypatch.setattr(googlemaps.Client, "geocode", mock_geocode)


@pytest.fixture(autouse=True)
def medaiwiki_api_call(monkeypatch):
    def mock_init(*args, **kwargs):
        pass
    monkeypatch.setattr(MediaWiki, "__init__", mock_init)

    def mock_geosearch(*args, **kwargs):
        return ['Stade de France',
                'Saint-Denis – Porte de Paris (Paris Métro)',
                'Lycée Suger', 'La Plaine–Stade de France station']
    monkeypatch.setattr(MediaWiki, "geosearch", mock_geosearch)

    def mock_summary(*args, **kwargs):
        return ("Le Stade de France est le plus grand stade de football "
                "français avec 80 698 places en configuration "
                "football/rugby. Il se situe dans le quartier de la "
                "Plaine Saint-Denis à Saint-Denis, dans la proche "
                "banlieue nord de Paris.")
    monkeypatch.setattr(MediaWiki, "summary", mock_summary)
