from langchain_community.vectorstores import FAISS

docs = [
    Document(page_content = "Global Warming is reason for the heated environment"),
    Document(page_content = "Global Warming is reason for the glacier melting"),
    Document(page_content = "We should not use AC and referigerator to reduce effect of global warming"),
    Document(page_content = "We should do afforestation because it is increasing the heat in environment")
]


