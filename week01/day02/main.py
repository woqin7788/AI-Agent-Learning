
customer_list = [
    {
        "company":"佛山市佰利建材",
        "country":"中国",
        "email":"123@qq.com"
    },
    {
        "company":"ABC Building",
        "country":"澳大利亚",
        "email":"abc@test.com"
    },
    {
        "company":"XYZ Construction",
        "country":"德国",
        "email":""
    }
]

def score_customer(customer):
    score = 0
    if customer.get("company"):
        score += 20
    if customer.get("country") == "澳大利亚":
        score +=30
    if customer.get("email"):
        score +=40
    return score

def get_level(score):
    if score >=80:
        return "重点开发"
    elif score >=60:
        return "普通开发"
    else:
        return "低价值"

def analyze_customer(customer):
    score =score_customer(customer)
    level = get_level(score)
    result = {
        "company": customer.get("company"),
        "country": customer.get("country"),
        "email": customer.get("email"),
        "score": score,
        "level": level
    }
    return result
result_list = []
for customer in customer_list:
    result_list.append(analyze_customer(customer))
print(result_list)

