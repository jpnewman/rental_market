import os
import sys

_basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfiguration(object):
    DEBUG = False
    TESTING = False

    ADMINS = frozenset(['admin@localhost'])
    SECRET_KEY = 'SecretKeyForSessionSigning'

    THREADS_PER_PAGE = 8

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "somethingimpossibletoguess"

    DATABASE = 'app.db'

    DATABASE_PATH = os.path.join(_basedir, DATABASE)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

    SCSS_STATIC_DIR = 'app/static'
    SCSS_ASSET_DIR = 'app/assets'

    ERROR_LOG_PATH = os.path.join(_basedir, 'logs/rental-market.log')

class TestConfiguration(BaseConfiguration):
    TESTING = True

    CSRF_ENABLED = False

    DATABASE = 'tests.db'
    DATABASE_PATH = os.path.join(_basedir, DATABASE)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # + DATABASE_PATH

class DebugConfiguration(BaseConfiguration):
    DEBUG = True
    if sys.platform == 'ios': # Pythonista
        DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True

    DEBUG_TB_ENABLED = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # DEBUG_TB_PANELS = (
    #     'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    #     'flask_debugtoolbar.panels.logger.LoggingPanel',
    #     'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    # )
