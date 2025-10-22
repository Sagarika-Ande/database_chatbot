def sanitize_user_input(text: str):
    """Remove potentially harmful SQL injections."""
    return text.replace(";", "").replace("--", "")
