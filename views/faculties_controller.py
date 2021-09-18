from flask import render_template
from config import app


class FacultiesController(object):

    @staticmethod
    @app.route('/faculties/list')
    def faculties_list():
        return render_template('faculties/list.html')
