from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("assessment_information.pdf")
docs = loader.load()

print(docs)
print(len(docs))

# IF it may have multiple pages then we could just simply access by 
print(docs[0].page_content)
# print(docs[3].metadata)



