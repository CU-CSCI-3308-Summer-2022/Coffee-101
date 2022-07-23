from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from coffee101.auth import login_required
from coffee101.db import get_db

bp = Blueprint('view', __name__)


def create_app():
    app = ...
    # existing code omitted

    from . import view
    app.register_blueprint(view.bp)
    app.add_url_rule('/', endpoint='index')

    return app


@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
    if request.method == 'POST':
        if 'select' in request.form:
            print('select')
            select = request.form['select']
            db = get_db()
            db.execute(
                'INSERT INTO record (user_id,drink_id)'
                ' VALUES (?, ?)',
                (g.user['id'], select)
            )
            db.commit()
            flash('Select successful!')
            return redirect(url_for('view.index'))
        if 'fav' in request.form:
            print('fav')
            fav = request.form['fav']
            db = get_db()
            db.execute(
                'INSERT INTO fav (user_id,drink_id)'
                ' VALUES (?, ?)',
                (g.user['id'], fav)
            )
            db.commit()
            flash('Add Favorite successful!')
            return redirect(url_for('view.index'))

    db = get_db()
    drinks = db.execute(
        'SELECT *'
        ' FROM drink'
    ).fetchall()
    return render_template('view/index.html', drinks=drinks)


@bp.route('/dashboard')
@login_required
def dashboard():
    db = get_db()
    users = db.execute(
        'SELECT COUNT(*) as userCount FROM user'
    ).fetchone()
    drinks = db.execute(
        'SELECT * FROM drink'
    ).fetchall()
    favs = db.execute(
        """
        Select f.drink_id, d.image, max(f.created)
        FROM fav f 
        JOIN user u ON f.user_id = u.id 
        JOIN drink d ON f.drink_id = d.id
        WHERE f.user_id = ?
        GROUP BY f.drink_id
        ORDER BY f.created desc
        LIMIT 3
        """, (g.user['id'],)
    ).fetchall()
    cups = db.execute(
        """
        Select count(*) as cupCount
        FROM record r 
        WHERE r.user_id = ? AND created > DATE('now','localtime', 'start of day')
        """, (g.user['id'],)
    ).fetchone()
    history = db.execute(
        """
        Select *
        FROM record r 
        JOIN user u ON r.user_id = u.id 
        JOIN drink d ON r.drink_id = d.id
        WHERE r.user_id = ? AND created BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime')
        ORDER BY r.created desc
        """, (g.user['id'],)
    ).fetchall()
    return render_template('view/dashboard.html', users=users, cups=cups, drinks=drinks, favs=favs, history=history)

