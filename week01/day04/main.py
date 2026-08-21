from loader import CustomerLoader
from analyzer import CustomerAnalyzer
from saver import CustomerSaver


loader = CustomerLoader()
analyzer = CustomerAnalyzer()
saver = CustomerSaver()


customers = loader.load("customers.json")


result_list = []

for customer in customers:

    customer_info = analyzer.analyze(customer)

    result_list.append(customer_info)


saver.save(
    result_list,
    "result.json"
)


print("分析完成")