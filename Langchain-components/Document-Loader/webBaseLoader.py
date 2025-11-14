from langchain_community.document_loaders import WebBaseLoader
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
    template="Answer the following question - {question} from the following text - \n {text}",
    input_variables=['question' , 'text']
)
parser = StrOutputParser()




url = 'https://en.wikipedia.org/wiki/Tamasha_(2015_film)'
loader = WebBaseLoader(url)

docs = loader.load()

#This can be used for printing purpose but for now we will do the Q/A with the gemini let's goooooo
# print(len(docs))
# print(docs[0].page_content)

#Here it is 
chain = prompt | model | parser
response = chain.invoke( {'question' : 'When did the movie Tamasha released ? ' ,
               'text' : docs[0].page_content} )
print(response)


response2 = chain.invoke( {'question' : 'How did the movie Tamasha ended ? ' ,
               'text' : docs[0].page_content} )
print(response2)