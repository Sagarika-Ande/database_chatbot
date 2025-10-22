import datetime

def log(message):
    """Print timestamped debug messages."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {message}")
