"""
级别排序:
    CRITICAL > ERROR > WARNING > INFO > DEBUG

debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上

info : 打印info,warning,error,critical级别的日志,确认一切按预期运行

warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作

error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能

critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行
"""
import logging
# 未输出
logging.debug("打印debug级别的日志")
logging.info("打印info级别的日志")
# 输出
logging.warning("打印warning级别的日志")
logging.error("打印error级别的日志")
logging.critical("打印critical级别的日志")


# 运行报出警告信息--------
# import openpyxl
# workbook = openpyxl.load_workbook("/Users/scan/Desktop/柠檬班/13/data.xlsx")
# sh = workbook.get_sheet_by_name("test")
# print(list(sh.rows))