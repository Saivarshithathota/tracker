
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Personal Expense Tracker")
st.write("Track your daily spending in one place.")

# Store expenses during the current session
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Expense entry form
st.header("➕ Add a New Expense")

with st.form("expense_form"):
    expense_date = st.date_input("Expense Date", value=date.today())
    amount = st.number_input(
        "Amount (₹)",
        min_value=0.01,
        value=100.0,
        step=10.0
    )
    category = st.selectbox(
        "Category",
        [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Health",
            "Education",
            "Entertainment",
            "Other"
        ]
    )
    description = st.text_input("Description")

    submitted = st.form_submit_button("Add Expense")

    if submitted:
        st.session_state.expenses.append({
            "Date": expense_date,
            "Amount": amount,
            "Category": category,
            "Description": description
        })
        st.success("Expense added successfully!")

# Dashboard
st.header("📊 Expense Dashboard")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)

    total = df["Amount"].sum()
    st.metric("Total Expenses", f"₹{total:,.2f}")

    st.subheader("Your Expenses")
    st.dataframe(df, use_container_width=True)

    st.subheader("Spending by Category")
    category_totals = df.groupby("Category")["Amount"].sum()
    st.bar_chart(category_totals)

else:
    st.metric("Total Expenses", "₹0.00")
    st.info("No expenses yet. Add your first expense above!")
