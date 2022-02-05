import logging


logger = logging.getLogger(__name__)  # logger wit name helper
logger.propagate = False  # default is True
logger.info("Hello from helper logger")
