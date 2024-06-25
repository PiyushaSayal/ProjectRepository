"""
from flask import Flask, request, jsonify
import pandas as pd

# Load the data
df = pd.read_csv('final_data.csv')

app = Flask(__name__)

# Function to handle queries
def simple_chatbot(user_query):
    if user_query == "What is the total revenue for Microsoft in 2023?":
        result = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2023)]['Total Revenue'].values[0]
        return f"The total revenue for Microsoft in 2023 is {result}."
    elif user_query == "How has Tesla's net income changed from 2022 to 2023?":
        income_2023 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2023)]['Net Income'].values[0]
        income_2022 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2022)]['Net Income'].values[0]
        change = income_2023 - income_2022
        return f"Tesla's net income has changed by {change} from 2022 to 2023."
    # Add more conditions for other predefined queries
    else:
        return "Sorry, I can only provide information on predefined queries."

@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query')
    response = simple_chatbot(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
"""

from flask import Flask, request, jsonify, render_template
import pandas as pd

# Load the data
df = pd.read_csv('final_data.csv')

# Print columns to verify
print(df.columns)

app = Flask(__name__)

# Function to handle queries
def simple_chatbot(user_query):
    try:
        if user_query == "What is the total revenue for Microsoft in 2023?":
            result = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2023)]['Total Revenue'].values[0]
            return f"The total revenue for Microsoft in 2023 is {result}."
        elif user_query == "How has Tesla's net income changed from 2022 to 2023?":
            income_2023 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2023)]['Net Income'].values[0]
            income_2022 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2022)]['Net Income'].values[0]
            change = income_2023 - income_2022
            return f"Tesla's net income has changed by {change} from 2022 to 2023."
        elif user_query == "What are the total assets of Apple in 2021?":
            result = df[(df['Company'] == 'Apple') & (df['Year'] == 2021)]['Total Assets'].values[0]
            return f"The total assets of Apple in 2021 are {result}."
        elif user_query == "What is the cash flow from operating activities for Microsoft in 2023?":
            result = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2023)]['Cash Flow from Operating Activities'].values[0]
            return f"The cash flow from operating activities for Microsoft in 2023 is {result}."
        elif user_query == "How much did Tesla's revenue grow in 2023?":
            result = df[(df['Company'] == 'Tesla') & (df['Year'] == 2023)]['Revenue Growth (%)'].values[0]
            return f"Tesla's revenue grew by {result}% in 2023."
        elif user_query == "What is the net income growth percentage for Apple in 2022?":
            result = df[(df['Company'] == 'Apple') & (df['Year'] == 2022)]['Net Income Growth (%)'].values[0]
            return f"The net income growth percentage for Apple in 2022 is {result}%."
        elif user_query == "What are the total liabilities of Microsoft in 2021?":
            result = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2021)]['Total Liabilities'].values[0]
            return f"The total liabilities of Microsoft in 2021 are {result}."
        elif user_query == "How has the assets growth percentage for Tesla changed from 2022 to 2023?":
            growth_2023 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2023)]['Assets Growth (%)'].values[0]
            growth_2022 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2022)]['Assets Growth (%)'].values[0]
            change = growth_2023 - growth_2022
            return f"The assets growth percentage for Tesla changed by {change}% from 2022 to 2023."
        elif user_query == "What is the CFO growth percentage for Apple in 2023?":
            result = df[(df['Company'] == 'Apple') & (df['Year'] == 2023)]['CFO Growth (%)'].values[0]
            return f"The CFO growth percentage for Apple in 2023 is {result}%."
        elif user_query == "What is the revenue growth percentage for Microsoft in 2023?":
            result = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2023)]['Revenue Growth (%)'].values[0]
            return f"The revenue growth percentage for Microsoft in 2023 is {result}%."
        elif user_query == "How did the liabilities growth percentage for Tesla change from 2022 to 2023?":
            growth_2023 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2023)]['Liabilities Growth (%)'].values[0]
            growth_2022 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2022)]['Liabilities Growth (%)'].values[0]
            change = growth_2023 - growth_2022
            return f"The liabilities growth percentage for Tesla changed by {change}% from 2022 to 2023."
        elif user_query == "What was Apple's net income in 2023?":
            result = df[(df['Company'] == 'Apple') & (df['Year'] == 2023)]['Net Income'].values[0]
            return f"Apple's net income in 2023 was {result}."
        elif user_query == "What are the total assets of Microsoft in 2022?":
            result = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2022)]['Total Assets'].values[0]
            return f"The total assets of Microsoft in 2022 are {result}."
        elif user_query == "What is the total revenue for Tesla in 2022?":
            result = df[(df['Company'] == 'Tesla') & (df['Year'] == 2022)]['Total Revenue'].values[0]
            return f"The total revenue for Tesla in 2022 is {result}."
        elif user_query == "How did the net income for Microsoft change from 2022 to 2023?":
            income_2023 = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2023)]['Net Income'].values[0]
            income_2022 = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2022)]['Net Income'].values[0]
            change = income_2023 - income_2022
            return f"Microsoft's net income changed by {change} from 2022 to 2023."
        elif user_query == "What is the assets growth percentage for Apple in 2021?":
            result = df[(df['Company'] == 'Apple') & (df['Year'] == 2021)]['Assets Growth (%)'].values[0]
            return f"The assets growth percentage for Apple in 2021 is {result}%."
        elif user_query == "How much did Microsoft's cash flow from operating activities change from 2022 to 2023?":
            cfo_2023 = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2023)]['Cash Flow from Operating Activities'].values[0]
            cfo_2022 = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2022)]['Cash Flow from Operating Activities'].values[0]
            change = cfo_2023 - cfo_2022
            return f"Microsoft's cash flow from operating activities changed by {change} from 2022 to 2023."
        elif user_query == "What is the liabilities growth percentage for Apple in 2021?":
            result = df[(df['Company'] == 'Apple') & (df['Year'] == 2021)]['Liabilities Growth (%)'].values[0]
            return f"The liabilities growth percentage for Apple in 2021 is {result}%."
        elif user_query == "What was Tesla's revenue in 2023?":
            result = df[(df['Company'] == 'Tesla') & (df['Year'] == 2023)]['Total Revenue'].values[0]
            return f"Tesla's revenue in 2023 was {result}."
        elif user_query == "How did the net income growth percentage for Apple change from 2022 to 2023?":
            growth_2023 = df[(df['Company'] == 'Apple') & (df['Year'] == 2023)]['Net Income Growth (%)'].values[0]
            growth_2022 = df[(df['Company'] == 'Apple') & (df['Year'] == 2022)]['Net Income Growth (%)'].values[0]
            change = growth_2023 - growth_2022
            return f"Apple's net income growth percentage changed by {change}% from 2022 to 2023."
        else:
            return "Sorry, I can only provide information on predefined queries."
    except KeyError as e:
        return f"Error: The column {e} does not exist in the dataset."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query')
    response = simple_chatbot(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
