#!/usr/bin/env python

import os
from app import create_app, db
from flask_script import Manager


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


@manager.command
def initdb():
    from sqlalchemy.sql import text
    cmd = """\
          CREATE EXTENSION hstore;
          CREATE TABLE urls ( id SERIAL, mapping HSTORE );
          INSERT INTO urls (mapping) VALUES ('');
          """
    db.engine.execute(text(cmd))


@manager.command
def key(key, value=None):
    from sqlalchemy.sql import text
    if value is None:
        q = "UPDATE urls SET mapping = delete(mapping, :key);"
    else:
        q = "UPDATE urls SET mapping = mapping || :key"
        key = '"%s"=>"%s"' % (key, value)
    db.engine.execute(text(q), key=key)


@manager.command
def list():
    from sqlalchemy.sql import text
    q = "SELECT (EACH(mapping)).* FROM urls;"
    results = db.engine.execute(text(q), key=key).fetchall()
    print("#" * 80)
    for result in results:
        print("http://data.qiime.org/{} => {}".format(*result))


if __name__ == '__main__':
    manager.run()
