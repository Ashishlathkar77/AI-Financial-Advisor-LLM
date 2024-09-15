# AI-Powered Financial Advisor 🏦

Welcome to the AI-Powered Financial Advisor project! This application leverages advanced AI models to provide personalized financial planning, tax optimization strategies, financial news summaries, and sentiment analysis of financial news articles. It’s designed to help users make informed financial decisions with ease.

## Features

- **Personalized Financial Plan**: Generate a step-by-step plan to achieve your financial goals based on your risk tolerance, investment preferences, and current savings.
- **Tax Optimization Strategy**: Receive tailored tax-saving strategies to optimize your investments and minimize tax liabilities.
- **Financial News Summary**: Get concise summaries of financial news articles to stay updated with the latest market trends.
- **Sentiment Intensity Analyzer**: Analyze the sentiment of financial news articles to gauge market sentiment.

## Deployed Application

You can access the deployed application [here](https://ai-financial-advisor-llm-fsu.streamlit.app/).

## Setup Instructions

To set up and run this project locally, follow these steps:

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Ashishlathkar77/AI-Financial-Advisor-LLM.git
   cd AI-Financial-Advisor-LLM

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv

3. **Activate the Virtual Environment**

   On Windows & On macOS/Linux:

    ```bash
    venv\Scripts\activate

    source venv/bin/activate
    
4. **Install the Required Packages**

    ```bash
    pip install -r requirements.txt
    
## Configuration

1. **Set Up API Keys**

You need an OpenAI API key for the application to work. Create a file named *.env* in the root directory of the project and add your API key:
    
    OPENAI_API_KEY=your-OpenAI-API-keys
    
## Running the Application

1. Start the Streamlit App

   ```bash
   streamlit run app.py
This will launch the application in your default web browser.

## Testing

The application can be tested by interacting with the following features:

- Personalized Financial Plan: Enter your risk tolerance, financial goal, investment preferences, goal amount, and current savings to generate a financial plan.
- Tax Optimization Strategy: Provide current savings and investment preferences to receive tax optimization strategies.
- Financial News Summary: Input a financial news URL to get a summary of the article.
- Sentiment Intensity Analyzer: Enter a financial news URL to analyze the sentiment of the article.

## Unit Testing
The project does not include specific unit tests at this time. However, you can add tests using frameworks like *unittest* or p*ytest* to test individual functions and ensure the accuracy of the financial calculations and AI responses.

## Idea:
The project presents a unique and innovative approach to financial advising by integrating AI-driven insights into financial planning, tax optimization, and sentiment analysis of news. The combination of these features provides users with a comprehensive tool to manage and enhance their financial decisions.

## Code Review:
The code is structured to ensure clarity and maintainability. It employs best practices such as modular design with separate functions for each feature, and the use of environment variables for sensitive information. The code is organized into a single app.py file, which integrates with external services like OpenAI and BeautifulSoup efficiently.

## Functionality:
The current version of the project works effectively, providing users with accurate financial plans, tax strategies, news summaries, and sentiment analysis. Each feature is accessible via a user-friendly interface in Streamlit, and the application handles various inputs gracefully.

## Application:
The project has significant real-world applicability. It serves as a comprehensive financial advisor tool that can assist users in making informed financial decisions, optimizing their tax strategies, and staying updated with market trends. The integration of AI and sentiment analysis makes it a valuable resource for individuals seeking personalized financial advice.

## Contributing
Contributions are welcome! If you have suggestions or find issues, please open an issue or submit a pull request.

## Acknowledgements
- *Streamlit* for the app deployment framework.
- *OpenAI* for providing the language models.
- *BeautifulSoup* for web scraping.

*Developed by Ashish Lathkar* 🧑‍💻
