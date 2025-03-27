import os
from pipeline import ArchitectureGenerationPipeline
from dotenv import load_dotenv
from langchain.globals import set_verbose

load_dotenv()
set_verbose(True)

def main():
    pdf_path = "CaseStudies/case_study_v2.pdf"
    
    # Create output folder if it doesn't exist
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    
    # Initialize the pipeline
    pipeline = ArchitectureGenerationPipeline()
    
    # Run the pipeline
    results = pipeline.run_pipeline(pdf_path)
    
    # Export Eraser diagram to a text file
    output_file_path = os.path.join(output_folder, "eraser_code.txt")
    
    with open(output_file_path, 'w') as f:
        f.write(results['eraser_diagram'])
    

if __name__ == "__main__":
    main()