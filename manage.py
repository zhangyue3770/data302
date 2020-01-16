# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import sys
from urllib.parse import urlparse
from pathlib import Path

from flask_script import Manager
import requests

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


@manager.command
def clone_remote_files(path):
    root = Path(path)
    for key, url in MAP.items():
        base = Path(key)
        p = root / base
        if str(base.parents[1]) == 'distro':
            p.parent.mkdir(parents=True, exist_ok=True)
            continue
        p.parent.mkdir(parents=True, exist_ok=True)
        if p.name in ('sample_metadata', 'sample_metadata.tsv'):
            continue
        print("Fetching %s" % p)
        r = requests.get(url, stream=True)
        with p.open('wb') as f:
            for stream_chunk in r.iter_content(chunk_size=1024):
                if stream_chunk:
                    f.write(stream_chunk)


if __name__ == '__main__':
    manager.run()
