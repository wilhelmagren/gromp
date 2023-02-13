import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '[%(asctime)s] [%(name)s] [%(levelname)s\t] %(message)s'
)

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

