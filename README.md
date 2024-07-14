# Savings Plan Calculator

This project implements a savings plan calculator using Python, Pandas, and Streamlit. It allows users to calculate and visualize a savings plan based on their monthly income, expenses, and savings percentage. Users can also exclude specific expense categories to see how it affects their savings plan dynamically.

## Project Structure

- **`saving_plans.py`**: Contains methods for calculating and displaying savings plans using Pandas dataframes.
  - `calculate_savings_plan(expenses, income, savings_percentage)`: Calculates savings based on proportional allocation.
  - `update_savings_plan(df_savings_plan, excluded_categories)`: Updates savings plan based on excluded categories.
  - `display_savings_plan(df_savings_plan)`: Displays savings plan in a tabular format.

- **`test.py`**: Main application using Streamlit to create an interactive UI for the savings plan calculator.
  - Allows users to input financial details, calculate savings plans, and dynamically exclude categories.

## Technologies Used

- **Python**
- **Pandas**: Used for data manipulation and analysis.
- **Streamlit**: Framework for creating interactive web applications.

## Approach

1. **Calculation of Savings Plan**:
   - The `calculate_savings_plan` function computes savings using a Pandas dataframe to handle expense data.
   - Savings are allocated proportionally across expense categories.

2. **Updating Savings Plan**:
   - The `update_savings_plan` function uses dataframe operations to exclude specific categories and reallocate savings.
   - Provides user feedback when no categories are selected for exclusion.

3. **User Interface**:
   - Implemented using Streamlit, providing sliders, input fields, and tables to interact with and visualize savings plans.

## Instructions to Reproduce Locally

1. **Clone the Repository**:
   - Clone this repository to your local machine using Git:

     ```bash
     git clone https://github.com/fatimamaatouk/savings-plan-calculator.git
     cd savings-plan-calculator
     ```

2. **Install Dependencies**:
   - Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
   - Install required Python packages using pip:

     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Application**:
   - Start the Streamlit app:

     ```bash
     streamlit run test.py
     ```

   - This will launch a local server. Open your web browser and go to `http://localhost:8501` to use the application.
