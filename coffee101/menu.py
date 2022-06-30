import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from coffee101.db import get_db

bp = Blueprint('coffee_menu', __name__, url_prefix='/coffee_menu')


@bp.route('/menu', methods=('GET', 'POST'))
def show_menu():

    return render_template('coffee_menu/menu.html')
