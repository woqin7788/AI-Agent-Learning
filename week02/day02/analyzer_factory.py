from week02.day02.registry import get


class AnalyzerFactory:

    @staticmethod
    def create(name, config):
        # 根据名称，从注册中心找到 Analyzer 类
        analyzer_class = get(name)

        # 没找到对应的 Analyzer
        if analyzer_class is None:
            raise ValueError(f"未知Analyzer: {name}")

        # 创建 Analyzer 对象
        return analyzer_class(config)