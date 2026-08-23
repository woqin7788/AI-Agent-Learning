from loader import CustomerLoader
from cleaner import CustomerCleaner
from deduplicator import CustomerDeduplicator
from validator import CustomerValidator
from analyzer import CustomerAnalyzer
from saver import CustomerSaver
from pipeline import CustomerPipeline
from config_loader import ConfigLoader

config_loader = ConfigLoader()
config = config_loader.load("config.json")

loader = CustomerLoader()
cleaner = CustomerCleaner()
deduplicator = CustomerDeduplicator()
validator = CustomerValidator(config)
analyzer = CustomerAnalyzer(config)
saver = CustomerSaver()


pipeline = CustomerPipeline(
    loader,
    cleaner,
    deduplicator,
    validator,
    analyzer,
    saver
)


pipeline.run(
    "customers.json"
)