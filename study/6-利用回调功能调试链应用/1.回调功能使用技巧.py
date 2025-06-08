from typing import Any, Optional, Union
from uuid import UUID

import dotenv
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.outputs import GenerationChunk, ChatGenerationChunk
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.callbacks import StdOutCallbackHandler, FileCallbackHandler,BaseCallbackHandler

dotenv.load_dotenv()

class LLMOpsCallBackHandler(BaseCallbackHandler):
    """自定义LLLMps回调处理器"""
    def on_chat_model_start(
        self,
        serialized: dict[str, Any],
        messages: list[list[BaseMessage]],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[list[str]] = None,
        metadata: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        print("开始调用模型")
        print("serialized",serialized)
        print("messages",messages)
    def on_llm_new_token(
        self,
        token: str,
        *,
        chunk: Optional[Union[GenerationChunk, ChatGenerationChunk]] = None,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        print("生成新token:",token)
        print("chunk",chunk)
        print("run_id",run_id)
prompt = ChatPromptTemplate.from_template("{query}")

llm = ChatTongyi()

chain = {"query": RunnablePassthrough()} | prompt | llm | StrOutputParser()

resp = chain.stream(
    "你好，我是谁",
    config={"callbacks": [StdOutCallbackHandler(),LLMOpsCallBackHandler()]})
for chunk in resp :
    pass
