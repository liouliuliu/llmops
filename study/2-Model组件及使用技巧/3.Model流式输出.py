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

ai_message = chatLLM.stream(prompt.invoke({"query":"你能简单的介绍下LLM和LLMOPS吗?"}))
for chunk in ai_message:
    print(chunk.content, end="")
