customers = [
    {
        "company":"佛山市佰利建材",
        "country":"中国",
        "email":"123@qq.com"
    },
    {
        "company":"ABC Building",
        "country":"Australia",
        "email":""
    }
]

def print_customer(customer):
    email = customer.get("email") or "暂无"
    print(
        f"""
    公司:{customer.get('company')}
    国家:{customer.get('country')}
    email:{email}
            """
    )
for customer in customers:
    print_customer(customer)