from loader import CustomerLoader
from analyzer import CustomerAnalyzer
from saver import CustomerSaver
from config_loader import ConfigLoader
from logger import logger
from exceptions import CustomerDataError

loader = CustomerLoader()
config_loader = ConfigLoader()
config = config_loader.load("config.json")
analyzer = CustomerAnalyzer(config)
saver = CustomerSaver()

try:
    customers = loader.load("customers.json")
except CustomerDataError as e:
    logger.error(e)
    customers = []

result_list = []

for customer in customers:

    customer_info = analyzer.analyze(customer)

    result_list.append(customer_info)

logger.info(f"此次分析{len(result_list)}个客户")
saver.save(
    result_list,
    "result.json"
)


logger.info("分析完成")