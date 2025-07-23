import logging
from project.common.handle_conf import conf

def creat_log(name='my_log', level="DEBUG", filename="log.log", f_level="DEBUG", w_level="DEBUG"):
    # 创建日志收集器
    log = logging.getLogger(name)
    # 设置收集器收集日志的等级
    log.setLevel(level)
    # 设置输出渠道
    # 1、输出到文件
    file_log = logging.FileHandler(filename=filename, encoding="utf-8")
    file_log.setLevel(f_level)
    log.addHandler(file_log)

    # 2.输出到控制台
    windows_log = logging.StreamHandler()
    windows_log.setLevel(w_level)
    log.addHandler(windows_log)
    # 设置日志输出格式
    formats = "%(asctime)s--%(filename)s-%(lineno)d---%(levelname)s:%(message)s"
    # 创建格式对象
    log_format = logging.Formatter(formats)
    # 为输出渠道设置输出格式
    file_log.setFormatter(log_format)
    windows_log.setFormatter(log_format)

    # 返回一个日志收集器
    return log


# 避免创建多个日志收集器而导致重复收集日志，可以只创建一个日志收集器
my_log = creat_log(
    name = conf.get("logging", 'name'),
    level = conf.get("logging", 'level'),
    filename = conf.get("logging", 'filename'),
    f_level = conf.get("logging", 'f_level'),
    w_level = conf.get("logging", 'w_level')
)