from db.connection import get_connection

def run_query(sql_query: str):
    """Execute an SQL query and return results as list of dictionaries."""
    conn = get_connection()
    if not conn:
        return [{"error": "Failed to connect to DB"}]
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql_query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        return [{"error": str(e)}]
