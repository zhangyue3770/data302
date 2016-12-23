# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from config import config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    import logging
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def main(path):
        q = "SELECT mapping -> :key FROM urls;"
        result = db.engine.execute(text(q), key=path).fetchone()
        if result[0]:
            return redirect(result[0])
        return '404 Not Found', 404

    return app
