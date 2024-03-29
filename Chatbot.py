from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import Tool,AgentExecutor,create_openai_functions_agent
from langchain import hub

import API_Keys

#Adding the OpenAI API Key to use the chatmodule of OpenAI
from API_Keys import open_api_key
#Adding the SerpAPI Key to be used as searching tool
from API_Keys import serpapi_key

#choose the prompt we want to use to guide the agent
prompt = hub.pull("hwchase17/openai-functions-agent")


#choosing SerpAPI as our searching tool
search=SerpAPIWrapper(serpapi_api_key= serpapi_key)
tools = [Tool(name="Search",func=search.run,description="useful when you need to answer questions about current events or new state of the world"),]

#Creating a memory for the agent to save chat history
memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True,output_key='output')

#Choosing the LLM model for the agent
llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0,openai_api_key=open_api_key)

#creating the agent
agent = create_openai_functions_agent(llm, tools, prompt)

#creating agent executor which will be used in the GUI to pass the inputs and getting outputs
agent_executer= AgentExecutor(agent=agent, tools=tools,memory=memory, verbose=True, handle_parsing_errors=True,return_intermediate_steps=True)


