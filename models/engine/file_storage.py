#!/usr/bin/env python3
import json


class FileStorage(object):
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
        
    def new(self, obj):
        FileStorage.__objects["{} {}"].format(obj.__class__.__name__, obj.id) = obj
        
    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects,f)
        
    def reload(self):
        with open(FileStorage.__file_path, "r") as f:
            json.load(f)