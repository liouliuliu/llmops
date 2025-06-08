import uuid

from langchain_community.chat_models import ChatTongyi
import dotenv
dotenv.load_dotenv()

llm = ChatTongyi()
llm.invoke("Hello, world!")

print(uuid.uuid4())