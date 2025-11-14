from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(
    path='Books',
    glob='*.pdf',  #Image attached hai usmai saare glob patterns available hai 
    loader_cls=PyPDFLoader
)

#now this process is time taken and memory inefficient 
#so we will not use load we will use lazy_load instead 
docs = loader.load()
print(len(docs))
print((docs[0].page_content))



for document in docs:
    print(document.metadata)
#ab yehb kya kr rha h ki pehle saare docs ko load kr rha hai aur fir humein unke metadata de rha hai 


#jabki yeh kya krega ki humein ek docs ko load kia fir uska metadata de dia aur hata dia fir dobara dusra aa rha aur same process ho rha hai 
docs2 = loader.lazy_load()
for document in docs2:
    print(document.metadata)