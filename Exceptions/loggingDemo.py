import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)
logging.critical("Critical error")
logging.error("Error occured")
#logging.warn("Warning message")
logging.info("Information message")
logging.debug("Debug message")