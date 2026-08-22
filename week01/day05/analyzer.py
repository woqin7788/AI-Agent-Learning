from customer import Customer

class CustomerAnalyzer:

    def __init__(self,config):
        self.config=config

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



    def get_level(self, score:int)->str:

        if score >= 80:

            return "重点开发"

        elif score >=60:

            return "普通开发"

        else:

            return "低价值"



    def analyze(self, customer:Customer)->dict:

        score = self.score_customer(customer)

        level = self.get_level(score)

        result = customer.get_info()

        result["score"] = score

        result["level"] = level

        return result