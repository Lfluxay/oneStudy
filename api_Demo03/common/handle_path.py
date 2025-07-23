# 路径处理操作
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用例数据路径
DATA_DIR = os.path.join(BASE_PATH, 'datas')

# 配置文件路径
CONF_DIR = os.path.join(BASE_PATH, 'config')

# 日志路径
LOG_DIR = os.path.join(BASE_PATH, 'logs')

# 报告路径
REPORT_DIR = os.path.join(BASE_PATH, 'reports')

# 用例路径
CASE_DIR = os.path.join(BASE_PATH, 'testcase')