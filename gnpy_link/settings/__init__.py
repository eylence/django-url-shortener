import os

if "PRODUCTION" in os.environ:
    from .production import *
else:
    from .development import *
