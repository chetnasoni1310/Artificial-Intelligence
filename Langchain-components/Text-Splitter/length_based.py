from langchain.text_splitter import CharacterTextSplitter

text = "From our conversations, you come across as a highly determined and fast-learning developer who genuinely wants to build a strong technical career. You’re not afraid to ask questions, even basic ones, because you care more about understanding deeply than pretending to know things. You push through errors instead of giving up, and you learn best by trying things hands-on. You think long-term, planning a path from React → Spring Boot → AI integrations like LangChain and RAG, which shows ambition and strategic thinking. Overall, you’re someone with the mindset, curiosity, and persistence needed to become a strong full-stack + AI developer."

splitter = CharacterTextSplitter(
            chunk_size = 100,
            chunk_overlap = 0,
            separator=''
        )

result = splitter.split_text(text)
print(result)