from customer import Customer

#数据清洗
class CustomerCleaner:
    def clean(self,custmoer:Customer) ->Customer:
        custmoer.country=custmoer.country.strip()
        custmoer.company=custmoer.company.strip()
        custmoer.email=custmoer.email.strip().lower()
        return custmoer
    def clean_list(self,custmoers:list[Customer]) ->list[Customer]:
        result=[]
        for custmoer in custmoers:
            result.append(self.clean(custmoer)
            )
        return result