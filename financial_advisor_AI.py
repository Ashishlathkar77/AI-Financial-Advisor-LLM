import streamlit as st
import requests
from bs4 import BeautifulSoup
import openai
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pytz
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI(api_key=OPENAI_API_KEY)
analyzer = SentimentIntensityAnalyzer()

def generate_financial_plan(risk_tolerance, financial_goal, investment_preferences, goal_amount, current_savings):
    prompt = f"""
    Given the following information:
    - Risk Tolerance: {risk_tolerance}
    - Financial Goal: {financial_goal}
    - Investment Preferences: {investment_preferences}
    - Goal Amount: {goal_amount}
    - Current Savings: {current_savings}

    Provide a detailed, step-by-step plan on how the user can achieve their financial goal. Include investment strategies, saving plans, and timelines.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a financial expert."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

def generate_tax_optimization_strategy(current_savings, investment_preferences):
    prompt = f"""
    Given the following investment preferences: {investment_preferences} and current savings: {current_savings}, provide a tax optimization strategy. Include suggestions like tax-loss harvesting, retirement account optimization, or other tax-saving tips.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a tax optimization expert."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

def summarize_financial_news(news_url):
    try:
        response = requests.get(news_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_text = ' '.join([p.text for p in soup.find_all('p')])

        prompt = f"""
        Summarize the following financial news article in a few sentences: {article_text}
        """
        
        ai_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial news summarizer."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return ai_response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error in summarizing the news: {str(e)}"

def analyze_sentiment(news_url):
    try:
        response = requests.get(news_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_text = ' '.join([p.text for p in soup.find_all('p')])

        sentiment = analyzer.polarity_scores(article_text)
        return sentiment
    except Exception as e:
        return f"Error in analyzing sentiment: {str(e)}"

from datetime import datetime
import pytz

def get_greeting():
    timezone = pytz.timezone('America/New_York')  
    now = datetime.now(timezone).hour

    if now < 12:
        return "Good morning 🌅"
    elif 12 <= now < 18:
        return "Good afternoon ☀️"
    else:
        return "Good evening 🌙"

def show_welcome_page():
    st.title("Welcome to the AI-Powered Financial Advisor 🏦")
    
    greeting = get_greeting()
    first_name = st.text_input("What's your first name?", "")
    
    if first_name:
        st.write(f"{greeting}, {first_name}! Welcome to our financial advisor app. 🎉")
        if st.button("Let's Go"):
            st.session_state.first_name = first_name
            st.session_state.show_main_app = True
    
def show_main_app():
    st.sidebar.title("AI-Powered Financial Advisor 🏦")
    option = st.sidebar.selectbox(
        "Choose a feature", 
        ["Personalized Financial Plan", "Tax Optimization Strategy", "Financial News Summary", "Sentiment Intensity Analyzer"]
    )

    if option == "Personalized Financial Plan":
        st.header("Personalized Financial Plan 💼")

        risk_tolerance = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])
        financial_goal = st.selectbox(
            "Financial Goal", 
            ["Save for retirement", "Buy a house", "Save for education", "Build an emergency fund", "Custom"]
        )

        if financial_goal == "Custom":
            goal_name = st.text_input("Custom Goal Name", "e.g., Start a business")
        else:
            goal_name = financial_goal

        investment_preferences = st.multiselect(
            "Investment Preferences", 
            ["Stocks", "Bonds", "Index Funds", "Mutual Funds", "Real Estate", "Cryptocurrency", "ETFs"]
        )

        goal_amount = st.number_input("Goal Amount", min_value=0, step=1000)
        current_savings = st.number_input("Current Savings", min_value=0, step=1000)

        if st.button("Generate Financial Plan"):
            financial_plan = generate_financial_plan(risk_tolerance, goal_name, investment_preferences, goal_amount, current_savings)
            st.subheader("Your Financial Plan 📈")
            st.write(financial_plan)

    elif option == "Tax Optimization Strategy":
        st.header("Tax Optimization Strategy 🧾")

        current_savings = st.number_input("Current Savings", min_value=0, step=1000)
        investment_preferences = st.multiselect(
            "Investment Preferences", 
            ["Stocks", "Bonds", "Index Funds", "Mutual Funds", "Real Estate", "Cryptocurrency", "ETFs"]
        )

        if st.button("Generate Tax Optimization Strategy"):
            tax_strategy = generate_tax_optimization_strategy(current_savings, investment_preferences)
            st.subheader("Your Tax Optimization Strategy 💡")
            st.write(tax_strategy)

    elif option == "Financial News Summary":
        st.header("Financial News Summary 📰")
        news_url = st.text_input("Enter Financial News URL")

        if st.button("Get Article Summary"):
            summary = summarize_financial_news(news_url)
            st.subheader("Article Summary 📝")
            st.write(summary)

    elif option == "Sentiment Intensity Analyzer":
        st.header("Sentiment Intensity Analyzer 📊")
        news_url = st.text_input("Enter Financial News URL")

        if st.button("Analyze Sentiment"):
            sentiment = analyze_sentiment(news_url)
            if isinstance(sentiment, dict):
                st.subheader("Sentiment Analysis Results 🧮")
                st.write("Positive: ", sentiment['pos'])
                st.write("Neutral: ", sentiment['neu'])
                st.write("Negative: ", sentiment['neg'])
                st.write("Compound: ", sentiment['compound'])
            else:
                st.write(sentiment)

def main():
    if 'show_main_app' not in st.session_state:
        st.session_state.show_main_app = False

    if 'first_name' not in st.session_state:
        show_welcome_page()
    else:
        if st.session_state.show_main_app:
            show_main_app()

    st.markdown(
        """
        <style>
        footer {
            visibility: hidden;
        }
        </style>
        <footer>
        <div style='text-align: center; padding: 10px; color: gray;'>
            Developed by {Ashish Lathkar} 🧑‍💻
        </div>
        </footer>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
