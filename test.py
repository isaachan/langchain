import os

os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "f6954bf2371ec855bf7a6a7b3bc188b932ba2848ed3457a3e390b919341000c6"

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

