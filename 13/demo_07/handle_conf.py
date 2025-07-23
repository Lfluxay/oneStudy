from configparser import ConfigParser


class Config(ConfigParser):
    # 创建对象的时候，直接加载配置文件中的内容
    def __init__(self, conf_file):
        super().__init__()
        self.read(conf_file, encoding='utf-8')

conf = Config(f"/Users/scan/Desktop/柠檬班/13/demo_07/config.ini")


# if __name__ == "__mian__":
    # conf = ConfigParser()
    # conf.read(f"/Users/scan/Desktop/柠檬班/13/demo_07/config.ini", encoding='utf-8')

    # conf = Config(f"/Users/scan/Desktop/柠檬班/13/demo_07/config.ini")

    # name = conf.get("logging", 'name')
    # level = conf.get("logging", 'level')
    # filename = conf.get("logging", 'log.log')
    # f_level = conf.get("logging", 'DEBUG')
    # w_level = conf.get("logging", 'DEBUG')