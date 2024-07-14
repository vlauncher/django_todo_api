from core.settings.base import *

if environ.get('DEBUG') == True:
    from core.settings.development import *
else:
    from core.settings.production import *