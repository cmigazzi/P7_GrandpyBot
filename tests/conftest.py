import pytest

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
        6: {"question": "Connaissez-vous l'adresse du Monoprix de Villeurbanne ?",
            "words": ["connaissez", "vous", "l", "adresse", "du",
                      "monoprix", "de", "villeurbanne"],
            "keywords": ["monoprix", "villeurbanne"]
            }
    }
