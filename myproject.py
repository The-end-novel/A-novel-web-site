#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comment
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Follow=Follow, Role=Role,
                Permission=Permission, Post=Post, Comment=Comment)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
