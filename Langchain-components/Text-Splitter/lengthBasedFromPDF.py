from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader



loader = PyPDFLoader(
    r"D:\Artificial-Intelligence\Langchain-components\Document-Loader\assessment_information.pdf"
)

docs = loader.load()
print(len(docs))

text = docs[0].page_content

splitter = CharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=0,
    separator='"""',
)

#not a good option here
response = splitter.split_text(text)
print(response)

print("")
print("")
print("")

#Better approach for document type things is ::
response2 = splitter.split_documents(docs)
print(response2)

print(response2[0])

print("")
print("")
print("")

print(response2[0].page_content)