import os

from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI


# global environment
os.environ["OPENAI_API_KEY"] = "sk-*********************************"

# llm initialization
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

while True:
    human_input = input("(human): ")
    human_input = [HumanMessage(content=human_input)]
    ai_output = llm(human_input)
    print(f"(ai): {ai_output.content}")