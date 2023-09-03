uni_data = [1,2,3,4,5,6,7,8,9,22,23,24,25,26,27,28,29,32,33,34,35,36,37,38.39]

import statistics

from util_logger import setup_logger

logger, logname = setup_logger(__file__)

mean = statistics.mean(uni_data)
median = statistics.median(uni_data)
mode = statistics.mode(uni_data)

logger.info(f"mean   = {mean:.2f}")
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")

var = statistics.variance(uni_data)
stdev = statistics.stdev(uni_data)
lowest = min(uni_data)
highest = max(uni_data)
range_ = highest - lowest

logger.info(f"var    = {var:.2f}")
logger.info(f"stdev  = {stdev:.2f}")
logger.info(f"lowest = {lowest:.2f}")
logger.info(f"highest= {highest:.2f}")
logger.info(f"range = {range_}")