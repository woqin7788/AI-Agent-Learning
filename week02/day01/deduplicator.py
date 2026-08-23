from customer import Customer
from logger import logger


class CustomerDeduplicator:
    #根据条件去重客户
    def remove_duplicate(self,customers:list[Customer]) ->list[Customer]:
        result=[]
        email_set = set()
        for customer in customers:
            if customer.email in email_set:
                continue
            email_set.add(customer.email)
            result.append(customer)
        logger.info(
            f"检测到{len(customers) - len(email_set)}个重复邮箱,剔除后还剩{len(email_set)}个客户！")
        return result