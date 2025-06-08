from typing import Any

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser

dotenv.load_dotenv()

# 1.构建组件
prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatTongyi()
parser = StrOutputParser()

# 2.创建链
chain = prompt | llm | parser

# 3.调用链
print(chain.invoke({"query": "你好,请讲一个冷笑话"}))