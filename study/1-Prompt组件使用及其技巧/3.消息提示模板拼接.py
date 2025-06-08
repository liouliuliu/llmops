from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

system_chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据用户的提示进行回复，我叫{username}"),
])

human_chat_prompt = ChatPromptTemplate.from_messages([
    ("human", "{question}"),
])

chat_prompt = system_chat_prompt + human_chat_prompt
print(chat_prompt.invoke({"username": "小明", "question": "今天天气怎么样？"}))
