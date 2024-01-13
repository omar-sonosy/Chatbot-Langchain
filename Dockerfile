FROM python:3.12

ADD GUI.py Chatbot.py API_Keys.py .

RUN pip install langchain langchain_openai langchain_community langchainhub customtkinter openai google-search-results


CMD ["python", "./GUI.py"]

