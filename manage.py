# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import sys
from urllib.parse import urlparse

from flask_script import Manager

from urls import MAP
from app import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def _template(k, v):
    return "{} =>\n  {}".format(k, v)


def _validate_url(url):
    # This is far from perfect, but should work fine for reasonable URLs
    parsed = urlparse(url)
    return bool(parsed.scheme or parsed.netloc)


@manager.command
def list():
    for key, val in MAP.items():
        print(_template(key, val))


@manager.command
def validate():
    errors = []
    for key, val in MAP.items():
        f_key = 'https://data.qiime2.org/%s' % key
        if not _validate_url(f_key) or not _validate_url(val):
            errors.append(_template(key, val))

    if errors:
        sys.exit('\n'.join(errors))


if __name__ == '__main__':
    manager.run()
