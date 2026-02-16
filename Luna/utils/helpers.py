# utils/helpers.py
from datetime import datetime
import json

def format_timestamp(dt: datetime = None) -> str:
    """Format datetime to readable string"""
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d %I:%M %p")

def save_json(data: dict, filepath: str):
    """Save dictionary to JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_json(filepath: str) -> dict:
    """Load JSON file to dictionary"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def clean_text(text: str) -> str:
    """Clean and normalize text"""
    return text.strip()

def time_ago(dt: datetime) -> str:
    """Convert datetime to 'time ago' string"""
    now = datetime.now()
    diff = now - dt
    
    seconds = diff.total_seconds()
    
    if seconds < 60:
        return "just now"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    else:
        days = int(seconds / 86400)
        return f"{days} day{'s' if days != 1 else ''} ago"