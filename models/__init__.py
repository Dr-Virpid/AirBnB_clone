#!/usr/bin/python3
"""
initialises our filestorage
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
