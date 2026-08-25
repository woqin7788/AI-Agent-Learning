from abc import ABC, abstractmethod


class AnalyzerInterface(ABC):

    @abstractmethod
    def analyze(self, customer):
        # 所有 Analyzer 都必须实现 analyze()
        pass