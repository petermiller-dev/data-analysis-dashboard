from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Read the CSV file
    df = pd.read_csv('Workout.csv')

    # Perform data analysis and generate visualizations
    # Example analysis:
    analysis_result = df.describe()

    # Generate a visualization
    chart = px.scatter(df, x='Exercise', y='Calories Burned')

    # Convert the visualization to HTML
    chart_html = chart.to_html(full_html=False)

    return render_template('result.html', result=analysis_result, chart=chart_html)

if __name__ == '__main__':
    app.run(debug=True)
