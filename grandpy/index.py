import os
import json

from flask import Blueprint, render_template, request

from .response_provider import ResponseProvider
from .requests_manager import RequestsManager
from .parser.exceptions import (InvalidQuestionException, NoSpacesException,
                                NotGeographicException)
from .parser.validator import QuestionValidator


bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.json["question"]
        try:
            qv = QuestionValidator(question)
            qv.spaces()
            qv.interrogation_mark()
            qv.geographic()
        except (InvalidQuestionException, NoSpacesException,
                NotGeographicException) as e:
            rp = ResponseProvider(e)
            message = rp.provider()
            response = {"is_valid": False,
                        "message": message}
        else:
            rm = RequestsManager(question)
            geocodes = rm.get_geocode()
            adress = rm.get_adress()
            summary = rm.get_summary()
            response = {"is_valid": True,
                        "geocodes":
                        {"lat": geocodes["lat"],
                         "lng": geocodes["lng"]
                         },
                        "adress": f"Et voilà l'adresse: {adress}.",
                        "summary": summary,
                        "transition": "T'ai-je déjà parlé de ce quartier ?"
                        }
        finally:
            json_response = json.dumps(response)
            return json_response

    else:
        rp = ResponseProvider()
        welcome = rp.provider()
        g_api_key = os.environ.get("G_API_KEY")
        return render_template('main.html',
                               welcome=welcome,
                               g_api_key=g_api_key)
