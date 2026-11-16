from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template("Answer this question: {question}")
model = ChatOpenAI(model="gpt-4o-mini")
messages = prompt.invoke({"question": "When do Python workshops meet?"})
answer = model.invoke(messages)
print(answer.content)
