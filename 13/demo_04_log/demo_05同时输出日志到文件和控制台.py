import logging
# 1.创建日志收集器
log = logging.getLogger("fluxay")

# 2.设置收集器的等级
log.setLevel("DEBUG")

# 3.设置输出日志的等级
# 3.1.创建日志输出到文件
log_hand = logging.FileHandler(filename="fluxay.log", encoding="utf-8")
log_hand.setLevel("DEBUG")
log.addHandler(log_hand)

# 3.2.输出到控制台
sh = logging.StreamHandler()
sh.setLevel("DEBUG")
log.addHandler(sh)


log.debug("打印debug级别的日志")
log.info("打印info级别的日志")
log.warning("打印warning级别的日志")
log.error("打印error级别的日志")
log.critical("打印critical级别的日志")