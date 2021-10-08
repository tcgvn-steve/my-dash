import dash
from flask_caching import Cache
import flask
# Diskcache
import diskcache
from dash.long_callback import DiskcacheLongCallbackManager

cache = diskcache.Cache("./cache")
long_callback_manager = DiskcacheLongCallbackManager(cache)

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                long_callback_manager=long_callback_manager)

# Caching and Signaling
# CACHE_CONFIG = {
#     # try 'filesystem' if you don't want to setup redis
#     'CACHE_TYPE': 'filesystem',
#     'CACHE_DIR': 'cache-directory'
# }
# cache = Cache()
# cache.init_app(server, config=CACHE_CONFIG)
