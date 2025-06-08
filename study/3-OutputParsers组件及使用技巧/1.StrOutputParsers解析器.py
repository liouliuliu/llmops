from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
import dotenv

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_template("{query}")

chatLLM = ChatTongyi(
    streaming=True
)

parser = StrOutputParser()
content = parser.invoke(chatLLM.invoke(prompt.invoke({"query":"现在是几点,请讲一个程序员的冷笑话"})))
print(content)