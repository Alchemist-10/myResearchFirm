import os
from crewai import Agent,Task, Crew,LLM,Process
from crewai_tools import SerperDevTool,ScrapeWebsiteTool
from dotenv import load_dotenv

load_dotenv()

llm=LLM(
    model="gemini-2.5-flash",
    temperature=0.7
    )
searchtool=SerperDevTool()
scrapetool=ScrapeWebsiteTool()

researcher=Agent(
    role='Senior Market reasearcher',
    goal='gather the most recent and rel' 
    'eveant news , press releases , '
    'and market sentiment regarding the {company}'
,  backstory="""
you work at a top tier hedge fund. you are a blood hound for data. you excel at using search engines to find the latest news articles and scraping htem
you never guess; you only provide data you have actually found online. """    
,
    verbose=True,
    allow_delegation=False,
    tools=[searchtool,scrapetool   ],
    llm=llm
)

finanalyst=Agent(
    role="senior financial analyst",
    goal="Analyze the raw data provided by the researcher and identify bullish (positive) or bearish (negative) trends.",
    backstory="""You are a cynical, highly experienced financial analyst. You look at raw news 
    and identify how it actually impacts a company's stock value. You separate market hype from reality.""",
    verbose=True,
    allow_delegation=True,
    llm=llm
)
investmentAdvisor=Agent(
    role="investment advisor",
    goal='Synthesize the research and analysis into a formatted, executive investment brief.',
    backstory="""You advise high-net-worth individuals. You take complex financial analysis 
    and write clear, decisive, and beautifully formatted investment reports. You always include 
    a final "BUY", "HOLD", or "SELL" recommendation based on the data.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)
#tasks
taskReasearch=Task(
    description="Search the internet for the latest news from the past 7 days regarding {company}. " \
    "Scrape the top 3 most relevant articles and summarize key events.",
    expected_output='An analytical breakdown of the news, categorizing it into Bullish and Bearish points.',
    agent=researcher

)

taskAnalyst=Task(
 description="Review the news summary provided by the researcher. Analyze the potential impact of these events on {company}'s market position. If the data is insufficient, ask the researcher for more.",
    expected_output='An analytical breakdown of the news, categorizing it into Bullish and Bearish points.',
    agent=finanalyst
)

taskReport = Task(
    description='Using the analysis, write a final Executive Investment Brief for {company}.' \
    ' Use markdown formatting, include bullet points, and provide a final recommendation.',
    expected_output='A polished, markdown-formatted investment brief ready for a client.',
    agent=investmentAdvisor
)

myResearchFirm=Crew(
    name="Akshay research firm",
    agents=[researcher,finanalyst,investmentAdvisor],
    tasks=[taskReasearch,taskAnalyst,taskReport],
    process=Process.sequential,
    memory=True,
    verbose=True
)

if __name__ == "__main__":
    targetCompany="Google"
    print(f"🚀 Starting research on: {targetCompany} using Gemini...\n")
    res=myResearchFirm.kickoff(inputs={'company': targetCompany})

    print("\n==============================================")
    print("✨ FINAL EXECUTIVE REPORT ✨")
    print("==============================================")
    print(res)