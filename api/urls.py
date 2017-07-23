from flask import Blueprint

urls = Blueprint('urls', __name__, url_prefix='/api')

@urls.route('/helloworld', methods=['GET', 'POST'])
def helloworld():
    return 'hi'