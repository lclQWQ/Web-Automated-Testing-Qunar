import logging.handlers


class GetLogger:
    _logger = None

    @classmethod
    def get_logger(cls, filepath, when="midnight", interval=1, backupCount=30):
        """

        :param filepath: 错误日志保存路径
        :param when: 日志文件记录范围，默认全天
        :param interval: 新日志文件生成，默认每天生成一个日志文件
        :param backupCount: 日志保存时限，默认30天，超过范围则自动覆盖之前的日志文件
        :return: 日志器
        """
        if cls._logger is None:
            # 获取日志器
            cls._logger = logging.getLogger()
            # 设置日志器默认级别
            cls._logger.setLevel(logging.INFO)

            # 获取处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=filepath + "error_log.log", when=when,
                                                           interval=interval, backupCount=backupCount, encoding='utf-8')
            th.setLevel(logging.ERROR)

            sh = logging.StreamHandler()

            # 获取格式器
            fmt = "%(asctime)s %(levelname)-8s [%(name)s] %(filename)s:%(lineno)d - %(message)s"
            formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")

            # 导入格式器
            th.setFormatter(formatter)
            sh.setFormatter(formatter)

            # 添加至日志器
            cls._logger.addHandler(th)
            cls._logger.addHandler(sh)

        return cls._logger
