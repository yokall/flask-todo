import datetime as dt

from marshmallow import Schema, fields


class ToDo():
    def __init__(self, description, done):
        self.description = description
        self.done = done
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<ToDo(name={self.description!r})>'.format(self=self)


class ToDoSchema(Schema):
    description = fields.Str()
    done = fields.Boolean()
    created_at = fields.Date()
    type = fields.Str()
