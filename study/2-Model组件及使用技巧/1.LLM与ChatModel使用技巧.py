from datetime import datetime

import dotenv
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate

load = dotenv.load_dotenv()

# 1.编排
prompt = ChatPromptTemplate.from_messages([
    ("system",  "你是OpenAI开发的聊天机器人，请根据用户的提示进行回复，当前时间为：{now}"),
    ("human","{query}")
]).partial(now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 2.创建大语言模型
# llm = ChatOpenAI()

chatLLM = ChatTongyi(
    streaming=True
)
# res = chatLLM.invoke(prompt.invoke({"query":"现在是几点,请讲一个程序员的冷笑话"}))
res = chatLLM.invoke(prompt.invoke({"query":"现在是几点,请讲一个程序员的冷笑话"}))
print(res.content)
print(res.type)
print(res.response_metadata)
# for r in res:
#     print("chat resp:", r)