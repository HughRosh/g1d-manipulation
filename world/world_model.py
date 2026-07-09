#!/usr/bin/env python3

"""
World Model

The world model is the single source of truth for all
objects the robot knows about.
"""

from dataclasses import dataclass


@dataclass
class WorldObject:
    name: str
    pose: object
    size: tuple


class WorldModel:

    def __init__(self):
        self.objects = {}

    def add(self, obj):
        self.objects[obj.name] = obj

    def get(self, name):
        return self.objects[name]

    def list_objects(self):
        return list(self.objects.keys())
