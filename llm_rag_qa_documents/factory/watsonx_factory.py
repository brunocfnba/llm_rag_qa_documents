import os
import json
from langchain_ibm import WatsonxLLM
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

WATSONX_APIKEY = os.getenv("WATSONX_APIKEY")
WATSONX_URL = os.getenv("WATSONX_URL")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")

class WatsonXFactory():
    def __init__(self):
        self.llm_model = "ibm-mistralai/mixtral-8x7b-instruct-v01-q"
        self.parameters = {
            "decoding_method": "greedy",
            "max_new_tokens": 900,
            "repetition_penalty": 1,
            "temperature": 0.0
        }

        self.watsonx_llm = WatsonxLLM(
            model_id=self.llm_model,
            url=WATSONX_URL,
            apikey=WATSONX_APIKEY,
            project_id=WATSONX_PROJECT_ID,
            params=self.parameters
        )
        """
        Initialize a new LLM from WatsonX.ai.

        :param llm_model: name of the llm model to be instanciated
        :type llm_model: String
        :param parameters: a set of parameters to tune the llm
        :type parameters: Dict
        """

    def ask_llm(self, prompt, prompt_question):
        """
        Sends a prompt along with a question to the LLM and retrieves an answer.

        :param prompt: a pre-defined prompt to provide context to the LLM
        :type prompt: PromptTemplate
        :param prompt_question: a question and other required inputs
        :type prompt_question: Dict
        """
        llm_chain = LLMChain(prompt=prompt, llm=self.watsonx_llm, verbose=True)
        get_answer = llm_chain.invoke(prompt_question)
        return get_answer
    
    def ask_llm_json(self, prompt, prompt_question):
        """
        Sends a prompt along with a question to the LLM and retrieves an answer in json (Dict) format.

        :param prompt: a pre-defined prompt to provide context to the LLM
        :type prompt: PromptTemplate
        :param prompt_question: a question and other required inputs
        :type prompt_question: Dict
        """
        get_answer = self.ask_llm(prompt, prompt_question)["text"]
        get_llm_json = json.loads(get_answer)
        return get_llm_json
    
    def ask_llm_stream(self, prompt_question):
        """
        Sends a prompt along with a question to the LLM and retrieves an answer leveraging stream.

        :param prompt_question: a question and other required inputs
        :type prompt_question: Dict
        """
        for chunk in self.watsonx_llm.stream(prompt_question):
            yield chunk
        