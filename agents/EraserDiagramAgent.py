from langchain.chains import LLMChain
from base_agent import BaseAgent
from prompts import EraserDiagramConversionPrompt
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

from langchain_community.document_loaders import UnstructuredMarkdownLoader

class EraserDiagramAgent(BaseAgent):
    def __init__(self, model_name="o3-mini", temperature=1.0):
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        
        # Initialize the chat model
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        self.prompt = ChatPromptTemplate.from_messages([EraserDiagramConversionPrompt.system_prompt, EraserDiagramConversionPrompt.user_prompt])
    
    def convert(self, json_steps: dict) -> str:
        file_path = "knowledge/eraser_knowledge.md"
        loader = UnstructuredMarkdownLoader(file_path=file_path)
        eraser_docs = loader.load()

        chat_history = self.memory.load_memory_variables({}).get("chat_history", "")
        
        chain = LLMChain(llm=self.llm, prompt=self.prompt)
        

        eraser_diagram = chain.run({
            "chat_history": chat_history,
            "json_steps": json_steps,
            "eraser_docs": eraser_docs
        })
        
        return eraser_diagram