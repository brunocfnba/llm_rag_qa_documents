import panel as pn
from llm_rag_qa_documents.factory.logger_factory import loggerFactory
from llm_rag_qa_documents.helpers.llm_helper import llmHelper

def main():
    """Starts the application. Initialize the webserver.
    """
    logger = loggerFactory().get_logger(f"llm_rag_qa_documents.{__name__}")
    logger.info("Starting Bot")
    llm = llmHelper()
    # answer = ""
    # for chunk in llm.talkToMe("what is the difference between eid and datamart?"):
    #     answer = "".join([answer, chunk])
    #     print(answer)
    #print(llm.talkToMe("how can I join EPM.FACT_REVENUE_COST_EXPENSE with DIM_TIME_PERIOD_FINANCE?"))

    def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
        message = ""
        for chunk in llm.talkToMe(contents):
            message += chunk 
            yield message


    chat_interface = pn.chat.ChatInterface(callback=callback, callback_exception="verbose")
    chat_interface.send(
        "Let's talk about your loaded documents!",
        user="Smart Bot",
        respond=False,
    )

    pn.serve(chat_interface)

    logger.info("Shutting Bot Down")

if __name__ == "__main__":
    main()