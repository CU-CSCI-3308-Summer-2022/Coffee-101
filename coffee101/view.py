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


@bp.route('/')
def index():
    db = get_db()
    drinks = db.execute(
        'SELECT *'
        ' FROM drink'
    ).fetchall()
    return render_template('view/index.html', drinks=drinks)


@bp.route('/dashboard')
def dashboard():
    db = get_db()
    users = db.execute(
        'SELECT COUNT(*) as userCount FROM user'
    ).fetchone()
    drinks = db.execute(
        'SELECT * FROM drink'
    ).fetchall()
    return render_template('view/dashboard.html', users=users, drinks=drinks)



# reference
"""
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('view.index'))

    return render_template('view/create.html')


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('view.index'))

    return render_template('view/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('view.index'))
    
"""
