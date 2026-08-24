from week02.day02.interfaces.analyzer_interface import AnalyzerInterface
from week02.day02.registry import register


class AIAnalyzer(AnalyzerInterface):

    def __init__(self, config):
        self.config = config
    def analyze(self, customer):

        return {
            "company": customer.company,
            "score": 100,
            "level": "AI重点客户"
        }
register(
    "AIAnalyzer",
    AIAnalyzer
)