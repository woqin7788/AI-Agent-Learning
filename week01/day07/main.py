from loader import CustomerLoader
from analyzer import CustomerAnalyzer
from saver import CustomerSaver
from config_loader import ConfigLoader
from logger import logger
from exceptions import CustomerDataError
from validator import CustomerValidator
from cleaner import CustomerCleaner
from deduplicator import CustomerDeduplicator

loader = CustomerLoader()
config_loader = ConfigLoader()
config = config_loader.load("config.json")
analyzer = CustomerAnalyzer(config)
saver = CustomerSaver()
validator = CustomerValidator(config)
cleaner = CustomerCleaner()
deduplicator=CustomerDeduplicator()

try:
    customers = loader.load("customers.json")
except CustomerDataError as e:
    logger.error(e)
    customers = []

result_list = []
customers = deduplicator.remove_duplicate(customers)
customers = cleaner.clean_list(customers)
for customer in customers:
    validation=validator.validate(customer)
    if not validation["valid"]:
        logger.warning(f"客户校验失败：{', '.join(validation["errors"])}")
        continue
    customer_info = analyzer.analyze(customer)

    result_list.append(customer_info)

logger.info(f"此次分析{len(result_list)}个客户")
saver.save(
    result_list,
    "result.json"
)


logger.info("分析完成")