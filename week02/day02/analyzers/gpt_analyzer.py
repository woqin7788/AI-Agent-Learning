from week02.day02.interfaces.analyzer_interface import AnalyzerInterface
from week02.day02.registry import register


class GPTAnalyzer(AnalyzerInterface):

    def __init__(self, config):
        self.config = config
    def analyze(self, customer):

        return {
            "company": customer.company,
            "score": 100,
            "level": "GPT重点客户"
        }
register(
    "GPTAnalyzer",
    GPTAnalyzer
)