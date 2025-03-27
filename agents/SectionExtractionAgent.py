
class SectionExtractionAgent():
    
    def extract_sections(self, text: str, section_names: list) -> dict:
        results = {}
        lines = text.split("\n")

        current_section = None
        section_content = []

        # List of possible section markers
        markers = [f"{i}. " for i in range(1, 10)] + [f"{i}." for i in range(1, 10)]

        for line in lines:
            line_stripped = line.strip()

            # Check if this line is a section header we're looking for
            found_new_section = False
            for section in section_names:
                for marker in markers:
                    if (
                        line_stripped == section
                        or line_stripped == f"{marker}{section}"
                        or line_stripped == f"{marker} {section}"
                    ):
                        # If we were collecting content for a previous section, save it
                        if current_section in section_names:
                            results[current_section] = "\n".join(
                                section_content
                            ).strip()

                        # Start new section
                        current_section = section
                        section_content = []
                        found_new_section = True
                        break

                # Also check for exact matches without numbering
                if line_stripped == section:
                    if current_section in section_names:
                        results[current_section] = "\n".join(section_content).strip()
                    current_section = section
                    section_content = []
                    found_new_section = True
                    break

            if found_new_section:
                continue

            # Add the line to the current section if we're tracking one
            if current_section in section_names:
                section_content.append(line)

        # Add the final section if we were collecting one
        if current_section in section_names:
            results[current_section] = "\n".join(section_content).strip()

        return results

    def process_sections(self, pdf_content):
        sections_to_extract = [
            "Solution Overview",
            "Solution Implementation"
        ]
        extracted_sections = self.extract_sections(pdf_content, sections_to_extract)
        return extracted_sections

    