# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from flask import Flask, redirect

from config import config
from urls import MAP


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def main(path):
        lookup = MAP.get(path)
        if lookup:
            return redirect(lookup)
        return '404 Not Found', 404

    return app
