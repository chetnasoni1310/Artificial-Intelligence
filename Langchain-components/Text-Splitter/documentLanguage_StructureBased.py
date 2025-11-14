from langchain.text_splitter import RecursiveCharacterTextSplitter ,Language

text = """  age = 22
if (age>=34):
    print("Want to be kid again  !! ")
elif (age>18 and age<23):    
    print("Don't want to live here !! ")
else :
    print("Want to grow upp !! ")

print("Thank you !!")    """

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size= 50,
    chunk_overlap = 0
)

response = splitter.split_text(text)
print(len(response))
print(response)


for str in response:
    print(str)