from datetime import datetime

from langchain_core.prompts import (PromptTemplate,
                                    ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    MessagesPlaceholder)
from langchain_core.messages import AIMessage

prompt = PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
print(prompt.format(subject="python"))
prompt_value = prompt.invoke({"subject": "程序员"})
print(prompt_value.to_string())
print(prompt_value.to_messages())

print("=========================================")

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据用户的提示进行回复，当前时间为：{now}"),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
]).partial(now=datetime.now())
chat_prompt_value = chat_prompt.invoke({
    "chat_history" : [
        ("human","我叫张三"),
        AIMessage("你好，我是OpenAI机器人，有什么可以帮到你")
    ],
    "subject":"程序员"
})
print(chat_prompt_value)
print(chat_prompt_value.to_string())