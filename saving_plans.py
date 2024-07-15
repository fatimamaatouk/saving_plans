import pandas as pd
import streamlit as st

def calculate_savings_plan(expenses, income, savings_percentage, flexibility_scores):
    # Convert expenses to a DataFrame
    df_expenses = pd.DataFrame(list(expenses.items()), columns=['Category', 'Amount'])
    
    # Calculate the savings goal
    savings_goal = income * savings_percentage / 100
    
    # Compute total expenses
    total_expenses = df_expenses['Amount'].sum()
    
    # Proportional allocation of savings
    df_expenses['Initial Savings'] = (df_expenses['Amount'] / total_expenses) * savings_goal
    
    # Adjust savings based on flexibility scores
    df_expenses['Flexibility'] = df_expenses['Category'].map(flexibility_scores)
    df_expenses['Adjusted Savings'] = df_expenses['Initial Savings'] * df_expenses['Flexibility']
    
    # Normalize adjusted savings to ensure they sum to the savings goal
    total_adjusted_savings = df_expenses['Adjusted Savings'].sum()
    df_expenses['Normalized Savings'] = (df_expenses['Adjusted Savings'] / total_adjusted_savings) * savings_goal
    
    return df_expenses

def update_savings_plan(df_savings_plan, excluded_categories):
    # Exclude specified categories
    excluded_df = df_savings_plan[df_savings_plan['Category'].isin(excluded_categories)]
    df_savings_plan = df_savings_plan[~df_savings_plan['Category'].isin(excluded_categories)]

    # Calculate the total excluded amount
    excluded_amount = excluded_df['Normalized Savings'].sum()
    
    if excluded_amount > 0:
        # Calculate the total remaining amount after exclusion
        # total_remaining = df_savings_plan['Normalized Savings'].sum()
        
        # Calculate the total flexibility score for the remaining categories
        total_flexibility = df_savings_plan['Flexibility'].sum()
        
        # Reallocate the excluded amount to remaining categories
        #df_savings_plan['Normalized Savings'] += (df_savings_plan['Normalized Savings'] / total_remaining) * excluded_amount
        df_savings_plan['Normalized Savings'] += (df_savings_plan['Flexibility'] / total_flexibility) * excluded_amount

    return df_savings_plan

def display_savings_plan(df_savings_plan):
    df_savings_plan['Normalized Savings'] = df_savings_plan['Normalized Savings'].round(2)
    total_savings = df_savings_plan['Normalized Savings'].sum().round(2)
    
    # Append the Total Savings as a new row
    total_row = pd.DataFrame([['Total Savings in $', total_savings]], columns=['Category', 'Normalized Savings'])
    st.table(pd.concat([df_savings_plan[['Category', 'Amount', 'Flexibility','Normalized Savings']], total_row], ignore_index=True))
