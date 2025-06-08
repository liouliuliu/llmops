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

# 2.定义一个链
class Chain:
    steps: list = []

    def __init__(self, steps: list):
        self.steps = steps

    def invoke(self, input : Any) -> Any:
        for step in self.steps:
            input = step.invoke(input)
            print("步骤：",step)
            print("输出：",input)
            print("==============================")
        return input

# 3.编排链
chain = Chain([prompt,llm,parser])


print(chain.invoke({"query":"你好,你是谁?"}))