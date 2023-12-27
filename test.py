import dotenv
dotenv.load_dotenv()

from langchain.agents import load_tools
from langchain.agents import initialize_agent

from langchain.llms import OpenAI
from langchain.agents import AgentType

llm = OpenAI(model_name="text-davinci-003", max_tokens=1024)

tools = load_tools(["serpapi"])

agent = initialize_agent(tools, 
                         llm, 
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("What's the date today? What great events have taken place today in history?")

