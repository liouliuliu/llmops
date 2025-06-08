import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough
from operator import itemgetter

dotenv.load_dotenv()


def retrieval(query: str) -> str:
    """一个模拟的检索器"""
    print("检索中:", query)
    return "我是张三"


prompt = ChatPromptTemplate.from_template(""" 请根据用户的问题进行回答，可以参考对应的上下文进行生成。

<context>
{context}
</context>

用户的提问是：{query}""")

llm = ChatTongyi()
parser = StrOutputParser()

chain = RunnablePassthrough.assign(context=lambda x: retrieval(x["query"])) | prompt | llm | parser

content = chain.invoke({"query":"你好，我是谁"})
print(content)
