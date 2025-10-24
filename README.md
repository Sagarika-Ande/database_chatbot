# database_chatbot

WORKIGN FLOW:
User Query
   ↓
LLM generates SQL (via prompt)
   ↓
SQL runs on MySQL database
   ↓
Results fetched and formatted
   ↓
Displayed in readable text


🧍‍♀️ Customer-related queries

Try questions about customers and their orders.

"Show all customers from Texas."
"List the first 5 customers and their email addresses."
"Which customers placed orders in May 2023?"
"Get the total number of customers in the database."
"Show all customers who placed more than 2 orders."

📦 Order-related queries

Check if the bot can query order info.

"Show all orders placed in 2023."
"List order IDs and dates handled by staff Sara."
"Show details of the latest 5 orders."
"Which orders are still pending or not shipped yet?"
"Get total number of orders handled by each staff."

👩‍💼 Staff-related queries

Ask about staff and their performance.

"Show all staff names and their store IDs."
"Which staff handled the most orders?"
"List all orders handled by John Smith."
"Show staff who are also managers."
"Count total number of staff working at the store."

🧠 Multi-table / Complex queries

These test joins and relationships between tables.

"Show customer names with the staff who handled their orders."
"List customers along with number of orders they placed."
"Show each staff member and total orders handled by them."
"List all orders with customer name, staff name, and order date."
"Which customers are handled by Sara Smith?"

🧾 Aggregate and summary queries

Useful to test GROUP BY and aggregate functions.

"Get total number of orders per state."
"Find the average number of orders handled per staff."
"Show the count of customers in each city."
"Get number of orders handled by each staff in 2024."
"Find the customer who placed the most orders."
