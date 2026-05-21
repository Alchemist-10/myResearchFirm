# Akshay Research Firm 🚀

An agentic AI system built with **CrewAI** that automates financial market research, analysis, and investment reporting. It utilizes Google's **Gemini 3 Flash** to power its logic and multiple agents to process real-time market data.

## 🤖 The Crew

The system consists of three specialized AI agents working together in a sequential process:

1.  **Senior Market Researcher**:
    - **Goal**: Gathers recent news, press releases, and market sentiment.
    - **Tools**: Uses `SerperDevTool` (Google Search) and `ScrapeWebsiteTool` to find and read real-time data.
    - **Constraint**: Never guesses; only provides verified online data.

2.  **Senior Financial Analyst**:
    - **Goal**: Analyzes raw data to identify bullish (positive) or bearish (negative) trends.
    - **Backstory**: A cynical expert who separates market hype from reality.

3.  **Investment Advisor**:
    - **Goal**: Synthesizes analysis into a formatted Executive Investment Brief.
    - **Output**: Provides a final "BUY", "HOLD", or "SELL" recommendation in markdown format.

## 🛠️ Tech Stack

- **Framework**: [CrewAI](https://www.crewai.com/)
- **LLM**: Google Gemini 2.5 Flash
- **Search**: Serper API
- **Scraping**: ScrapeWebsiteTool

## 🚀 Setup Instructions

### 1. Prerequisites

- Python installed.
- A virtual environment is recommended (e.g., `learnagenticcrewai`).

### 2. Environment Variables

Create a `.env` file in the root directory and add your API keys:

```env
# CrewAI and Tools
SERPER_API_KEY=your_serper_key_here

# Google Gemini API
GEMINI_API_KEY=your_gemini_key_here
```

### 3. Installation

Install the necessary dependencies:

```powershell
pip install crewai crewai_tools python-dotenv
```

### 4. Running the Agent

Run the script to start researching a company (default set to "Google"):

```powershell
python reasearch_firm.py
```

## 📂 Project Structure

- [reasearch_firm.py](reasearch_firm.py): The main script containing agent definitions, tasks, and the crew execution.
- [.gitignore](.gitignore): Configured to ignore sensitive files like `.env` and virtual environments.
- [readme.md](readme.md): Project documentation.
