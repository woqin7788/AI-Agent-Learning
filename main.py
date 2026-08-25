from loader import CustomerLoader
from cleaner import CustomerCleaner
from deduplicator import CustomerDeduplicator
from validator import CustomerValidator
from saver import CustomerSaver
from pipeline import CustomerPipeline
from config_loader import ConfigLoader
import analyzer_factory
from plugin_loader import AnalyzerPluginLoader


config_loader = ConfigLoader()
config = config_loader.load("config.json")
AnalyzerPluginLoader.load("analyzers")
loader = CustomerLoader()
# 从配置文件获取当前要使用的 Analyzer 名称
analyzer_name = config["analyzer"]
cleaner = CustomerCleaner()
deduplicator = CustomerDeduplicator()
validator = CustomerValidator(config)
analyzer = analyzer_factory.AnalyzerFactory.create(
    analyzer_name,config )
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