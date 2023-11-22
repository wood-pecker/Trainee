from flask import render_template
from flask import Blueprint, render_template


errors_bp = Blueprint('route', __name__)


@errors_bp.errorhandler(404)
def page_not_found(error):
    return render_template('templates/page_not_found.html'), 404
