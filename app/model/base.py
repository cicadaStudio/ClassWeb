from contextlib import contextmanager
from flask import current_app
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy

__all__ = ['db', 'Base']


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self, throw=True):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            current_app.logger.exception('%r' % e)
            if throw:
                raise e


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)