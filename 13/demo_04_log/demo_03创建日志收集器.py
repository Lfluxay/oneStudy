
"""
日志收集器：
    logging.getLogger()
    参数不传，返回的是默认参数
    若传入参数，会创建一个新的日志收集器

"""


import logging
# 创建日志收集器
log = logging.getLogger("fluxay")

# 设置收集器的等级
log.setLevel("DEBUG")

# 设置输出日志的等级
# 1.创建日志输出渠道，输出到控制台
sh = logging.StreamHandler()
sh.setLevel("DEBUG")
# 2.将输出渠道绑定到日志收集器上
log.addHandler(sh)


log.debug("打印debug级别的日志")
log.info("打印info级别的日志")
log.warning("打印warning级别的日志")
log.error("打印error级别的日志")
log.critical("打印critical级别的日志")