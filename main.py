from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import query_rag

model = OllamaLLM(model="llama2")

PROMPT= """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context in a brief: {question}
"""

def main(question:str):
    prompt_template = ChatPromptTemplate.from_template(PROMPT)
    chain = prompt_template | model
    results = query_rag(question)
    context = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    response_text  = chain.invoke({"context": context, "question": question})
    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text