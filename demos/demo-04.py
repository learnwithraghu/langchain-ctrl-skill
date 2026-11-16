from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

DOCUMENTS = {
    "refund": "Students may request a refund within 14 days of enrollment.",
    "workshop": "Python workshops meet on Tuesdays at 6 PM online.",
}


def retrieve(question):
    return next(
        (text for keyword, text in DOCUMENTS.items() if keyword in question.lower()),
        "No matching information.",
    )


def main():
    question = "How do I get a refund?"
    prompt = ChatPromptTemplate.from_template(
        "Answer using only this context. If it does not help, say you don't know.\n"
        "Context: {context}\nQuestion: {question}"
    )
    model = ChatOpenAI(model="gpt-4o-mini")
    chain = prompt | model | StrOutputParser()

    context = retrieve(question)
    print(f"Retrieved: {context}")
    print(chain.invoke({"context": context, "question": question}))


if __name__ == "__main__":
    main()
