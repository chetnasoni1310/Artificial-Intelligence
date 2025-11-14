from langchain_community.retrievers import WikipediaRetriever
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os




# Load env
load_dotenv()



# Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2
)



# Prompt Template
prompt = PromptTemplate(
    template="""
Use the following Wikipedia information to answer the query:

Query: {query}

Wikipedia Data:
{context}

Answer:

And if you don't know the answer , If the context does not contain the answer, state that you could not find the information in the provided context.
""",
    input_variables=["query", "context"]
)

parser = StrOutputParser()


# Wikipedia retriever
retriever = WikipediaRetriever(
    lang='en',
    top_k_results=2
)


# User query
query = "Virat Kohli"


# Retrieve documents
docs = retriever.invoke(query)



# Combine retrieved text
#    You go to Wikipedia →   Copy two paragraphs →   Paste them into Gemini →   Ask a question.
context = "\n\n".join([doc.page_content for doc in docs])



# Run RAG chain
chain = prompt | model | parser
response = chain.invoke({"query": query, "context": context})



# Print final answer
print("\n===== FINAL ANSWER =====\n")
print(response)



# Print retrieved chunks
print("\n===== WIKIPEDIA RESULTS =====")
for i, document in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(document.page_content[:500], "...")
