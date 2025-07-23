from demo_04_log.handle_log import creat_log

log = creat_log()

log.debug("打印debug级别的日志")
log.info("打印info级别的日志")
log.warning("打印warning级别的日志")
log.error("打印error级别的日志")
log.critical("打印critical级别的日志")