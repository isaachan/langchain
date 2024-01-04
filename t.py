from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOllama

# chat_model = ChatOllama(
#     model="llama2:7b",
#     format="json", 
#     callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
# )

chat_model = ChatOllama(
    model="llama2:7b", 
    # base_url = 'http://127.0.0.1:11434'
)

from langchain.schema import HumanMessage

messages = [
    HumanMessage(
        content="""
        你是一位很会讲故事的人，这里有一段文字“桌子上有一辆汽车模型”，请你根据这句话讲个故事，并且带点儿幽默诙谐的那种。字数控制在100字以内。一定要用中文。
        """
    )
]

chat_model_response = chat_model(messages)

print(chat_model_response)


# from langchain.chains import create_extraction_chain
# from langchain_experimental.llms.ollama_functions import OllamaFunctions


# # Schema
# schema = {
#     "properties": {
#         "name": {"type": "string"},
#         "height": {"type": "integer"},
#         "hair_color": {"type": "string"},
#     },
#     "required": ["name", "height"],
# }

# # Input
# input = """Alex is 5 feet tall. Claudia is 1 feet taller than Alex and jumps higher than him. Claudia is a brunette and Alex is blonde."""

# # Run chain
# llm = OllamaFunctions(model="mistral", temperature=0)
# chain = create_extraction_chain(schema, llm)
# chain.run(input)