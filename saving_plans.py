import pandas as pd
import streamlit as st

def calculate_savings_plan(expenses, income, savings_percentage):
    # Convert expenses to a Dataframe
    df_expenses = pd.DataFrame(list(expenses.items()), columns=['Category', 'Amount'])
    
    # Calculate the savings goal
    savings_goal = income * savings_percentage / 100
    
    # Compute total expenses
    total_expenses = df_expenses['Amount'].sum()
    
    # Proportional allocation of savings
    df_expenses['Savings'] = (df_expenses['Amount'] / total_expenses) * savings_goal
    
    return df_expenses

def update_savings_plan(df_savings_plan, excluded_categories):        
    # Exclude specified categories
    excluded_df = df_savings_plan[df_savings_plan['Category'].isin(excluded_categories)]
    df_savings_plan = df_savings_plan[~df_savings_plan['Category'].isin(excluded_categories)]
    
    # Calculate the total excluded amount
    excluded_amount = excluded_df['Savings'].sum()
    if excluded_amount > 0:   
            # Calculate the total remaining amount after exclusion
            total_remaining = df_savings_plan['Savings'].sum()

            # Reallocate the excluded amount to remaining categories
            df_savings_plan['Savings'] += (df_savings_plan['Savings'] / total_remaining) * excluded_amount

    return df_savings_plan

def display_savings_plan(df_savings_plan):
    df_savings_plan['Savings'] = df_savings_plan['Savings'].round(2)
    total_savings = df_savings_plan['Savings'].sum().round(2)
    
    # Append the Total Savings as a new row
    total_row = pd.DataFrame([['Total Savings in $',total_savings]], columns=['Category','Savings'])
    st.table(pd.concat([df_savings_plan[['Category','Savings']],total_row],ignore_index=True))