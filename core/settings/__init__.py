# backend/settings/__init__.py

import os


if os.getenv('DEBUG') == 'False':
    from .production import *
else:
    from .development import *