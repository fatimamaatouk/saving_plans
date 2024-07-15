from saving_plans import calculate_savings_plan, update_savings_plan, display_savings_plan
import streamlit as st

def main():
    st.title("Savings Plan Calculator")
    income = st.number_input("Enter your monthly income (in $):", min_value=0, step=1000)
    savings_percentage = st.slider("Enter the percentage of income to save(%):", min_value=0, max_value=100, step=1)
    
    st.write("Enter your monthly expenses (in $) and Set flexibility scores for each category (Higher Scores means More Flexible):")
    expenses = {}
    flexibility_scores = {}
    
    categories = ["rent", "groceries", "dining_out", "entertainment", "utilities", "other"]
    for category in categories:
        col1,col2 = st.columns(2)
        with col1:
            expenses[category] = st.number_input(f"Amount for {category}:", min_value=0, step=50)
        with col2:
            flexibility_scores[category] = st.slider(f"Flexibility Score for {category}:", min_value=0.0, step=0.1, max_value=1.0,value=0.5)
    
    excluded_categories = st.multiselect("Calculate categories to exclude from savings:", options=categories)
    
    if st.button("Calculate Savings Plan"):
        savings_plan = calculate_savings_plan(expenses, income, savings_percentage, flexibility_scores)
        st.subheader("Initial Savings Plan($): ")
        display_savings_plan(savings_plan)
        
        if excluded_categories:
            updated_savings_plan = update_savings_plan(savings_plan.copy(), excluded_categories)
            st.subheader("Updated Saving Plans($):")
            display_savings_plan(updated_savings_plan)
        else:
            st.subheader("No categories were excluded from the savings plan.")
    
if __name__ == "__main__":
    main()    
