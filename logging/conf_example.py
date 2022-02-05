import logging
import logging.config

logging.config.fileConfig("logging/logging.conf")

logger = logging.getLogger("simpleExample")
logger.debug("this is a debug message")
