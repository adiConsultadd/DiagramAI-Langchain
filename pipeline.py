from agents.PDFExtractionAgent import PDFExtractionAgent
from agents.SectionExtractionAgent import SectionExtractionAgent
from agents.SectionToJSONAgent import SectionToJSONAgent
from agents.RuleValidationAgent import RuleValidationAgent
from agents.EraserDiagramAgent import EraserDiagramAgent

class ArchitectureGenerationPipeline:
    def __init__(self):
        self.pdf_agent = PDFExtractionAgent()
        self.section_agent = SectionExtractionAgent()
        self.json_agent = SectionToJSONAgent()
        self.rule_agent = RuleValidationAgent()
        self.eraser_agent = EraserDiagramAgent()
    
    def run_pipeline(self, pdf_path):
        # 1. Extract PDF content
        pdf_content = self.pdf_agent.parse_pdf(pdf_path)
        
        # 2. Extract specific sections
        sections = self.section_agent.process_sections(pdf_content)
        
        # 3. Convert sections to JSON
        json_steps = self.json_agent.convert_to_json(sections)
        
        # 4. Validate rules
        validated_steps = self.rule_agent.validate(json_steps)

        # 5. Convert to Eraser diagram
        eraser_diagram = self.eraser_agent.convert(json_steps)
        
        return {
            'pdf_content': pdf_content,
            'sections': sections,
            'json_steps': json_steps,
            'validated_steps': validated_steps,
            'eraser_diagram': eraser_diagram
        }