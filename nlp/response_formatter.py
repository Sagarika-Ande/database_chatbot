def format_response(results):
    """Convert SQL query results into readable text."""
    if not results:
        return "No records found."

    if "error" in results[0]:
        return f"Error: {results[0]['error']}"

    # Format as table-like output
    keys = results[0].keys()
    response = "Here are the results:\n\n"
    response += "\t".join(keys) + "\n"
    response += "-" * 50 + "\n"

    for row in results:
        response += "\t".join(str(row[k]) for k in keys) + "\n"

    return response
