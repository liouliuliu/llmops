import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

dotenv.load_dotenv()

# 1.编排prompt
joke_prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话,尽可能短一些")
poem_prompt = ChatPromptTemplate.from_template("请写一首关于{subject}的诗,尽可能短一些")

# 2.创建模型
llm = ChatTongyi()

# 3.解析器
parser = StrOutputParser()
# 4。编排链
joke_chain = joke_prompt | llm | parser
poem_chain = poem_prompt | llm | parser

# 5.创建并行链
# map_chain = RunnableParallel({
#     "joke": joke_chain,
#     "poem": poem_chain
# })

map_chain = RunnableParallel(
    joke= joke_chain,
    poem= poem_chain
)
res = map_chain.invoke({"subject": "猫"})
print(res)