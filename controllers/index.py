from flask import *
import datetime

index = Blueprint('index', __name__, template_folder='templates')

@index.route('/', methods=['GET'])
def index_route():
    options = {'date' : datetime.date.today()}

    return render_template('index.html', **options)
