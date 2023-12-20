from django.template.loader import render_to_string
from datetime import datetime
from os.path import splitext


def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])
