import os
import json

from flask import Blueprint, render_template, request

from .response_provider import ResponseProvider
from .requests_manager import RequestsManager


bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.json["question"]
        print(question)
        rm = RequestsManager(question)
        geocodes = rm.get_geocode()
        summary = rm.get_summary()
        response = {"geocodes":
                    {"lat": geocodes["lat"],
                     "lng": geocodes["lng"]
                     },
                    "summary": summary
                    }
        json_response = json.dumps(response)
        return json_response

    else:
        rp = ResponseProvider()
        welcome = rp.welcome()
        g_api_key = os.environ.get("G_API_KEY")
        return render_template('main.html',
                               welcome=welcome,
                               g_api_key=g_api_key)
