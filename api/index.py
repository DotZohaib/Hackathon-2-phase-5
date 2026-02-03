import sys
import os

# Add the backend directory to sys.path so that imports like "from app..." work correctly
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from backend.main import app

# Vercel Serverless Function Entrypoint
# The 'app' object is automatically detected by Vercel's Python runtime
# if it's a WSGI or ASGI application.
