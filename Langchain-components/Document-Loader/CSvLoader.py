from langchain_community.document_loaders import CSVLoader
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





loader = CSVLoader('industry.csv')

docs = loader.load()
print(len(docs))
print((docs[0]))




chain = prompt | model | parser
response = chain.invoke({'question':'which is most leading industry from these ?',
                         'text':docs})
print(response)


response2 = chain.invoke({'question':'Group the related industries together',
                         'text':docs})
print(response2)