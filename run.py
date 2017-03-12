#!/usr/bin/env python3
from app import app, db

db.create_all()
app.run()
