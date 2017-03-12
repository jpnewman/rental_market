
# flake8: noqa
__author__ = 'John Paul Newman'

import os
import sys

from flask import Flask, request, render_template, send_from_directory
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DebugConfiguration')

# Scss
if sys.platform != 'ios': # Not Pythonista
    from flask_scss import Scss
    Scss(app)

# Database
db = SQLAlchemy(app)

# Debug Toolbar
toolbar = DebugToolbarExtension(app)

# Register module blueprint
from app.properties.views import mod as propertiesModule
app.register_blueprint(propertiesModule)

from app.agencies.views import mod as agenciesModule
app.register_blueprint(agenciesModule)

from app.agents.views import mod as agentsModule
app.register_blueprint(agentsModule)

# from app.viewings.views import mod as viewingsModule
# app.register_blueprint(viewingsModule)


# Controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.route("/")
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(400)
def key_error(e):
    app.logger.warning('Invalid request resulted in KeyError', exc_info=e)
    return render_template('400.html'), 400


@app.errorhandler(500)
def internal_server_error(e):
    app.logger.warning('An unhandled exception is being displayed to the end user', exc_info=e)
    return render_template('generic.html'), 500


@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('An unhandled exception is being displayed to the end user', exc_info=e)
    return render_template('generic.html'), 500


@app.before_request
def log_entry():
    app.logger.debug("Handling request")


@app.teardown_request
def log_exit(exc):
    app.logger.debug("Finished handling request", exc_info=exc)


# Logging
import logging


class ContextualFilter(logging.Filter):
    def filter(self, log_record):
        log_record.url = request.path
        log_record.method = request.method
        log_record.ip = request.environ.get("REMOTE_ADDR")

        return True

context_provider = ContextualFilter()
app.logger.addFilter(context_provider)
del app.logger.handlers[:]

handler = logging.StreamHandler()

log_format = "%(asctime)s\t%(levelname)s\t%(ip)s\t%(method)s\t%(url)s\t%(message)s"
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)

app.logger.addHandler(handler)

from logging import ERROR, DEBUG
from logging.handlers import TimedRotatingFileHandler

# Only set up a file handler if we know where to put the logs
if app.config.get("ERROR_LOG_PATH"):

    log_folder = os.path.dirname(app.config["ERROR_LOG_PATH"])
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # Create one file for each day. Delete logs over 7 days old.
    file_handler = TimedRotatingFileHandler(app.config["ERROR_LOG_PATH"], when="D", backupCount=7)

    file_formatter = logging.Formatter(log_format)

    # Filter out all log messages that are lower than Error.
    file_handler.setLevel(DEBUG) # ERROR

    file_handler.setFormatter(file_formatter)
    app.logger.addHandler(file_handler)
