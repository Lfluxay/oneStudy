import logging

log = logging.getLogger()
# 设置收集
log.setLevel("DEBUG")


logging.debug("打印debug级别的日志")
logging.info("打印info级别的日志")
logging.warning("打印warning级别的日志")
logging.error("打印error级别的日志")
logging.critical("打印critical级别的日志")