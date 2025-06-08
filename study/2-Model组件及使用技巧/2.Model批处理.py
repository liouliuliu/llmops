from datetime import datetime

import dotenv
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate

load = dotenv.load_dotenv()

# 1.编排
prompt = ChatPromptTemplate.from_messages([
    ("system",  "你是聊天机器人，请根据用户的提示进行回复，当前时间为：{now}"),
    ("human","{query}")
]).partial(now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 2.创建大语言模型

chatLLM = ChatTongyi(
    streaming=True
)

ai_message = chatLLM.batch([
    prompt.invoke({"query":"你好，你是谁？"}),
    prompt.invoke({"query":"现在是几点,请讲一个程序员的冷笑话"}),
])
for message in ai_message:
    print(message.content)
    print("================")
