from langchain_core.prompts import PromptTemplate
from jinja2 import Template
from llm_rag_qa_documents.factory.logger_factory import loggerFactory

class promptsConfig():
    def __init__(self):

        self.logger = loggerFactory().get_logger(__name__)
        self.docs_template_jinja = Template("""

        {
            "task": "The rules should be strictly followed ",
            "taskRules": [
                    "If you don't know the answer, just say that you don't know, don't try to make up an answer.",
                    "only use the context provided and the question to generate your output",
                    "Elaborate your output answer, use the whole context provided",
                    "don't use more than 6 sentences in your output",
                    "instead of mentioning you found the answer in the context, show the answer"
            ]
        }

        Begin of Context: {{context}}  End of Context

        Question: {{input}}
        """)
    
    def get_prompt_ready(self, prompt_name, values):
        if prompt_name == "docs":
            prompt = self.docs_template_jinja.render(input=values["input"], context=values["context"])
        else:
            self.logger.info("Prompt value not found")
            Exception(ValueError("Prompt value not found"))

        return prompt