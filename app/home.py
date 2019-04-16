import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.db import get_db

bp = Blueprint('home', __name__)

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/home')
def home():
    return render_template('home.html')