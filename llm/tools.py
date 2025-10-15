# chatbot_project/llm/tools.py
from langchain.tools import tool
from database import queries

@tool
def get_database_schema_summary() -> str:
    """
    Returns a summary of the database schema, including tables (orders, customers, staffs)
    and their respective columns with data types.
    This tool should be used first to understand the database structure before attempting to query.
    """
    return queries.get_database_schema_summary()

@tool
def execute_database_query(sql_query: str) -> str:
    """
    Executes a read-only SQL SELECT query against the database and returns the results.
    This tool is designed for flexible data retrieval when specific functions are not available.
    The SQL query must be a valid SELECT statement.
    Example: "SELECT * FROM customers WHERE customer_id = 1;"
    """
    print(f"\n--- Executing SQL Query: {sql_query} ---\n")
    result = queries.get_raw_sql_query_result(sql_query)
    return str(result) # LLM needs string output

# Example of more specific tools (you can add many more based on expected queries)
@tool
def get_customer_orders(customer_id: int) -> str:
    """
    Retrieves all orders placed by a specific customer, identified by their customer_id.
    Returns a list of order details including order_id, order_date, amount, and staff details.
    """
    print(f"\n--- Getting orders for customer ID: {customer_id} ---\n")
    result = queries.get_orders_by_customer_id(customer_id)
    return str(result)

@tool
def get_staff_orders(staff_id: int) -> str:
    """
    Retrieves all orders handled by a specific staff member, identified by their staff_id.
    Returns a list of order details including order_id, order_date, amount, and customer details.
    """
    print(f"\n--- Getting orders for staff ID: {staff_id} ---\n")
    result = queries.get_orders_by_staff_id(staff_id)
    return str(result)

@tool
def describe_customer(customer_id: int) -> str:
    """
    Retrieves detailed information for a specific customer, identified by their customer_id.
    Returns all available columns for the customer.
    """
    print(f"\n--- Describing customer ID: {customer_id} ---\n")
    result = queries.get_customer_by_id(customer_id)
    return str(result)

@tool
def get_total_number_of_orders() -> str:
    """
    Returns the total count of all orders in the database.
    """
    print("\n--- Getting total number of orders ---\n")
    result = queries.get_total_orders_count()
    return str(result)

# You can add a tool to list customers if needed, but 'execute_database_query' can also handle it.
@tool
def list_all_customers_summary() -> str:
    """
    Retrieves a summary list of all customers, including their customer_id, first_name, and last_name.
    Limited to 10 customers for brevity.
    """
    print("\n--- Listing all customers summary ---\n")
    result = queries.get_all_customers()
    return str(result)


# List all tools available to the agent
ALL_TOOLS = [
    get_database_schema_summary,
    execute_database_query,
    get_customer_orders,
    get_staff_orders,
    describe_customer,
    get_total_number_of_orders,
    list_all_customers_summary
]