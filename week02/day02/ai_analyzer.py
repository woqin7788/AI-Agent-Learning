from interfaces.analyzer_interface import AnalyzerInterface


class AIAnalyzer(AnalyzerInterface):


    def analyze(self, customer):

        return {
            "company": customer.company,
            "score": 100,
            "level": "AI重点客户"
        }