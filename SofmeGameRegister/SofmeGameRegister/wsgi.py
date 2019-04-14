"""
WSGI config for SofmeGameRegister project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
#import sys
import sys  # 追加


from django.core.wsgi import get_wsgi_application
sys.path.append('/var/www/python/SofmeGameRegister')             # 追加
#sys.path.append('/var/www/python/SofmeGameRegister/SofmeGameRegister')   # 追加

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SofmeGameRegister.settings")

application = get_wsgi_application()
