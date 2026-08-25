from customer import Customer

#数据清洗
class CustomerCleaner:
    def clean(self,customer:Customer) ->Customer:
        if customer.country:
            customer.country=customer.country.strip()
        if customer.company:
            customer.company=customer.company.strip()
        if customer.email:
            customer.email=customer.email.strip().lower()
        return customer
    def clean_list(self,customers:list[Customer]) ->list[Customer]:
        result=[]
        for customer in customers:
            result.append(self.clean(customer)
            )
        return result