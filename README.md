
*   **Natural Language to SQL:** Translate user questions into appropriate SQL queries.
*   **Database Interaction:** Query `orders`, `customers`, and `staffs` tables.
*   **Extensible:** Easily add more specific database query functions and LLM tools.
*   **LangChain Agent:** Uses `create_tool_calling_agent` for robust tool selection and execution.
*   **Google Gemini Pro:** Utilizes Google's powerful LLM.
*   **Modular Design:** Clear separation of database, LLM, and agent logic.

*   Example Queries You Can Ask
1."How many orders are there?"
2."Show me all customers."
3."Who is customer with ID 1?"
4."What orders did customer 5 place?"
5."Which orders were handled by staff member 3?"
6."Can you describe customer 10?"
7."Show me orders from 2023-01-01 to 2023-01-31." (If you add get_orders_in_date_range tool)
8."Who are the top 3 customers by order count?" (If you add get_top_customers_by_order_count tool)
