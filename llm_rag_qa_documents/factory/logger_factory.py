import sys
import logging


class loggerFactory():
    """Return Logger with Correct Formatting"""

    def __init__(self, main_logger="llm_rag_qa_documents"):
        """Initialize logger factory"""
        self.main_logger_name = main_logger
        self.level = logging.INFO
        self.format = self.set_log_format()
        self.root_logger = self.initialize_root_logger()

    def initialize_root_logger(self):
        """Initialize the root logger so logs can propagate to it
        """
        console_format = logging.Formatter(self.format)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(console_format)

        logger = logging.getLogger(self.main_logger_name)
        logger.propagate = False
        logger.setLevel(self.level)

        if not logger.handlers:
            logger.addHandler(console_handler)

        return logger

    def set_log_format(self):
        """
        Set log format.
        """
        log_format = """
            {
                "Message": %(message)s, 
                "Metadata": { 
                    "Timestamp": %(asctime)s, 
                    "LoggerType": %(levelname)s, 
                    "LoggerName": %(name)s , 
                    "Filename" : %(filename)s, 
                    "Function" : %(funcName)s, 
                    "Line":  %(lineno)d
                    }
            }"""
        return log_format

    def get_logger(self, name):
        """Get logger
        :param name: Logger name
        :type name: string
        """
        return logging.getLogger(name)