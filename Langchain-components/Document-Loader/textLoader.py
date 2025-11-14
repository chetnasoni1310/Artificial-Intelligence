from langchain_community.document_loaders import TextLoader
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os




load_dotenv()


# LLM Model (Gemini)
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2
)

prompt = PromptTemplate(
    template="Write a summary for the following poem - \n {poem}",
    input_variables=['poem']
)
parser = StrOutputParser()



loader = TextLoader('poem.txt' , encoding='utf-8')
docs = loader.load()
# print(docs) 
#print ho jayega but with all the info 
print(type(docs)) #always be a list 
print(len(docs))  #abhi toh bss ek hi hai poem hi 
print(docs[0])
print(docs[0].page_content)
print(docs[0].metadata)
print(type(docs[0]))


chain = prompt | model | parser
summary = chain.invoke({'poem' : docs[0].page_content})
print(summary)