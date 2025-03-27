from langchain.chains import LLMChain
from base_agent import BaseAgent
from prompts import RuleValidationPrompt
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain


class RuleValidationAgent():
    def __init__(self, model_name="o3-mini", temperature=1.0):
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        
        # Initialize the chat model
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        self.prompt = ChatPromptTemplate.from_messages([RuleValidationPrompt.system_prompt, RuleValidationPrompt.user_prompt])
    
    def validate(self, content: dict) -> dict:
        validation_results = {}
        
        chat_history = self.memory.load_memory_variables({}).get("chat_history", "")
        
        chain = LLMChain(llm=self.llm, prompt=self.prompt)
        
        # Process each section
        result = chain.run({
            "chat_history": chat_history,
            "jsonContent": content,
        })        

        return result