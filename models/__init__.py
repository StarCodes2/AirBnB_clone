#!/usr/bin/python3
"""Recreate objects from the serialized json string representation saved using
   the storage method defined in module file_stotage, once the program launch,
   if any exists."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
