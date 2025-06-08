import dotenv
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel,Field

dotenv.load_dotenv()

# 1.创建一个类，用于告诉模型，这个模型返回的是一个json格式的数据
class Joke(BaseModel):
    # 冷笑话
    joke : str = Field(description="回答用户的冷笑话")
    # 冷笑话的笑点
    punchline : str = Field(description="这个冷笑话的笑点")
parser = JsonOutputParser(pydantic_object=Joke)

# 2.构建一个模板
prompt = ChatPromptTemplate.from_template("请根据用户的提问进行回答 . \n{format_instructions}\n{query}").partial(format_instructions=parser.get_format_instructions())
# print(prompt.format(query="讲一个程序员的冷笑话"))

# 3.构建一个大语言模型
llm = ChatTongyi()
# 4.传递提示并解析
joke = parser.invoke(llm.invoke(prompt.invoke({"query":"讲一个程序员的冷笑话"})))
print(joke)
print(type(joke))
print(joke.get("punchline"))