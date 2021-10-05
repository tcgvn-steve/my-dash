import dash
from flask_caching import Cache
import os
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server
# Caching and Signaling
CACHE_CONFIG = {
    # try 'filesystem' if you don't want to setup redis
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'redis://172.17.75.15:6379')
}
cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)
