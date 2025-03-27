from langchain.chains import LLMChain
from prompts import SectionToJSONConversionPrompt
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_community.document_loaders.csv_loader import CSVLoader


class SectionToJSONAgent():
    def __init__(self, model_name="o3-mini", temperature=1.0):
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        
        # Initialize the chat model
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        self.prompt = ChatPromptTemplate.from_messages([SectionToJSONConversionPrompt.system_prompt, SectionToJSONConversionPrompt.user_prompt])
    
    def convert_to_json(self, sections: dict) -> dict:
        file_path = "knowledge/eraser_icons.csv"
        loader = CSVLoader(file_path=file_path)
        icon_data = loader.load()
        
        json_result = {
            "solution": {
                "title": "Solution Title",
                "overview": "High-level description of the proposed solution",
            },
            "components": [
                {
                    "id": "component-1",
                    "name": "Component Name",
                    "description": "Detailed description of the component's functionality",
                    "technology": "Technologies used (e.g., HL7, FHIR, AWS)",
                    "icon": "appropriate-eraser-icon",
                    "category": "infrastructure|application|data|security|integration|user",
                    "parent_id": "null",
                }
            ],
            "groups": [
                {
                    "id": "group-1",
                    "name": "Group Name",
                    "description": "Description of the group's purpose",
                    "icon": "appropriate-eraser-icon",
                    "components": ["component-id-1", "component-id-2"],
                }
            ],
            "connections": [
                {
                    "source_id": "component-1 or group-1",
                    "target_id": "component-2 or group-2",
                    "label": "Description of the connection",
                    "type": "data-flow|dependency|integration|api|reference",
                    "direction": "unidirectional|bidirectional",
                    "icon": "appropriate-eraser-icon",
                }
            ],
        }
        
        chat_history = self.memory.load_memory_variables({}).get("chat_history", "")
        
        chain = LLMChain(llm=self.llm, prompt=self.prompt)
        
        result = chain.run({
            "chat_history": chat_history,
            "sections": sections,
            "json_result": json_result,
            "icon_data": icon_data
        })

        return result





