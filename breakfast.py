from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage
load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.5)
messages=[SystemMessage(content="You are expert chef who specialized in simple cooking"),
          HumanMessage(content="Give me 5 breakfast ideas:")]
response = llm.invoke(messages)
print(messages[1].content)
print(response.content)
