from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain
class BaseAgent:
    def __init__(self, system_prompt, user_prompt, model_name="o3-mini", temperature=1.0):
        # Initialize memory for chat history
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        
        # Initialize the chat model
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        
        # Create system and user prompt templates
        system_template = SystemMessagePromptTemplate.from_template(system_prompt)
        user_template = HumanMessagePromptTemplate.from_template(user_prompt)
        
        # Combine them into a chat prompt template
        self.prompt = ChatPromptTemplate.from_messages([system_template, user_template])
    
    def process(self, context, question="No specific question"):
        """Generic method to process input using LLM"""
        # Retrieve conversation history from memory
        chat_history = self.memory.load_memory_variables({}).get("chat_history", "")
        
        # Create the LLMChain instance
        chain = LLMChain(llm=self.llm, prompt=self.prompt)
        
        # Execute the chain
        result = chain.run({
            "chat_history": chat_history,
            "context": context,
            "question": question
        })
        
        return result


