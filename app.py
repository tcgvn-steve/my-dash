import dash
from flask_caching import Cache
import flask
server = flask.Flask(__name__)
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Caching and Signaling
CACHE_CONFIG = {
    # try 'filesystem' if you don't want to setup redis
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
}
cache = Cache()
cache.init_app(server, config=CACHE_CONFIG)
