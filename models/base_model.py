#!/usr/bin/env python3

from datetime import datetime
import uuid

class BaseModel(object):

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        pass

    def save(self):
        pass

    def to_dict(self):
        pass

