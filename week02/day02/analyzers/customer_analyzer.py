from week02.day02.customer import Customer
from week02.day02.registry import register
from week02.day02.interfaces.analyzer_interface import AnalyzerInterface

class CustomerAnalyzer(AnalyzerInterface):

    def __init__(self,config):
        self.config=config
    #给客户打分
    def score_customer(self, customer:Customer)->int:

        score = 0
        rules=self.config["score_rules"]

        if customer.company:
            score += rules["company"]

        country_score = rules["country"].get(customer.country,0)

        if customer.email:
            score += rules["email"]
        score += country_score
        return score


    #按照分数给客户打等级标签
    def get_level(self, score:int)->str:

        if score >= 80:

            return "重点开发"

        elif score >=60:

            return "普通开发"

        else:

            return "低价值"


    #分析客户质量
    def analyze(self, customer:Customer)->dict:

        score = self.score_customer(customer)

        level = self.get_level(score)

        result = customer.get_info()

        result["score"] = score

        result["level"] = level

        return result
    def list_analyze(self, customers:list[Customer])->list[dict]:
        results=[]
        for customer in customers:
            score = self.score_customer(customer)
            level = self.get_level(score)
            result = customer.get_info()
            result["score"] = score
            result["level"] = level
            results.append(result)
        return results


register(
    "CustomerAnalyzer",
    CustomerAnalyzer
)