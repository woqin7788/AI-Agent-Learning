class Customer:

    def __init__(self, company, country, email):

        self.company = company
        self.country = country
        self.email = email
    def get_info(self) -> dict:
        return {
            "company": self.company,
            "country": self.country,
            "email": self.email
        }


customer_list = [

    Customer(
        "佛山市佰利建材",
        "中国",
        "123@qq.com"
    ),

    Customer(
        "ABC Building",
        "澳大利亚",
        "abc@test.com"
    ),

    Customer(
        "XYZ Construction",
        "德国",
        ""
    )

]
class CustomerAnalyzer:

    def score_customer(self, customer:Customer)-> int:

        score = 0

        if customer.company:
            score += 20

        if customer.country == "澳大利亚":
            score += 30

        if customer.email:
            score += 40

        return score


    def get_level(self, score)-> str:

        if score >= 80:
            return "重点开发"

        elif score >= 60:
            return "普通开发"

        else:
            return "低价值"


    def analyze(self, customer:Customer) -> dict:

        score = self.score_customer(customer)

        level = self.get_level(score)

        result = customer.get_info()
        result["score"] = score
        result["level"] = level

        return result
customerAnalyzer = CustomerAnalyzer()
for customer in customer_list:
    result = customerAnalyzer.analyze(customer)
    print(result)
