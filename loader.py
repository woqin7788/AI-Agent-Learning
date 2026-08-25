import json
from json import JSONDecodeError
from exceptions import CustomerDataError
from logger import logger
from customer import Customer



class CustomerLoader:

    #加载文件读取客户信息
    def load(self, file_path:str)->list:
        logger.info(f"开始分析客户数据，客户文件地址：{file_path}")
        customers=[]
        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:
                data=json.load(file)
                for item in data:
                    customer=Customer(
                        item.get("company"),
                        item.get("country"),
                        item.get("email") or "暂无",
                    )
                    customer.tags.append("重点关注")
                    customers.append(customer)

        except FileNotFoundError as e:
            raise CustomerDataError(f"文件不存在:{file_path}")


        except JSONDecodeError as e:
            raise CustomerDataError(f"JSON格式错误:{e}")

        logger.info(f"加载出{len(customers)}个客户")
        return customers