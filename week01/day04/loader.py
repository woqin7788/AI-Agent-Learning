import json

from customer import Customer



class CustomerLoader:


    def load(self, file_path:str)->list:


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
                        item.get("email") or "暂无"
                    )

                    customers.append(customer)


        except FileNotFoundError:

            print("文件不存在")
            raise


        except json.JSONDecodeError:

            print("JSON格式错误")
            raise


        return customers