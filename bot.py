from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3:latest")

template = '''
Answer the following question
Here is the conversation history : {context}
Question : {question}
Answer : 
'''
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model


def conversation():
    context = ""
    print("Welcome to the LLAma chatbot \n Type bye to exit.")
    while True:
        user_query = input("You : ")
        if user_query.lower() == 'bye':
            print("bye")
            break
        response = chain.invoke({"context" : context, "question":user_query})
        print("LlamaBOT : ", response)
        context += f'\n User: {user_query} \n AI{response}'
# response = model.invoke(input="hey llama, how are you ?")
# print(response)

if __name__ == "__main__":
    conversation()