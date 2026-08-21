from customer import Customer


class CustomerAnalyzer:


    def score_customer(self, customer:Customer)->int:

        score = 0

        if customer.company:
            score += 20

        if customer.country == "澳大利亚":
            score += 30

        if customer.email:
            score += 40

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