import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_openrouter import ChatOpenRouter

prompt = ChatPromptTemplate.from_template("Answer this question: {question}")


def get_model(provider):
    if provider == "openai":
        return ChatOpenAI(model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"))
    if provider == "openrouter":
        return ChatOpenRouter(
            model=os.environ.get("OPENROUTER_MODEL", "openrouter/free")
        )
    raise ValueError("LLM_PROVIDER must be 'openai' or 'openrouter'")


def main():
    model = get_model(os.environ.get("LLM_PROVIDER", "openai"))
    chain = prompt | model | StrOutputParser()
    print(chain.invoke({"question": "When do Python workshops meet?"}))


if __name__ == "__main__":
    main()
