import streamlit as st
import pandas as pd

# --- TASK 1: Build the App ---

# 1. Displays a title and a short subheader
st.title("Sales Summary Dashboard")
st.subheader("An interactive app to view sales data by category.")

# 2. Creates a hardcoded pandas DataFrame (5 rows, 3 columns)
data = {
    "Product": ["Laptop", "Smartphone", "Desk Chair", "Monitor", "Headphones"],
    "Category": ["Electronics", "Electronics", "Furniture", "Electronics", "Accessories"],
    "Sales": [1200, 800, 300, 450, 150]
}
df = pd.DataFrame(data)

# --- TASK 2: Add a Sidebar ---

# 1. Move the selectbox filter into a sidebar
# 2. Get unique categories for the dropdown
categories = df["Category"].unique()
selected_category = st.sidebar.selectbox("Select a Category", categories)

# Filter the DataFrame based on selection
filtered_df = df[df["Category"] == selected_category]

# 3. Main content area: Show the filtered table
st.write(f"### Sales Data for: {selected_category}")
st.dataframe(filtered_df)

# 4. Main content area: Show a line chart of sales values
st.write("### Sales Trend")
# Note: Streamlit's line_chart needs the index or a specific column for the Y-axis
st.line_chart(filtered_df.set_index("Product")["Sales"])