from logger import logger
class CustomerPipeline:
    def __init__(
            self,
            loader,
            cleaner,
            deduplicator,
            validator,
            analyzer,
            saver
    ):
        self.loader = loader
        self.cleaner = cleaner
        self.deduplicator = deduplicator
        self.validator = validator
        self.analyzer = analyzer
        self.saver = saver

    def run(self, file_path):

        customers = self.loader.load(
            file_path
        )

        customers = self.cleaner.clean_list(
            customers
        )

        customers = self.deduplicator.remove_duplicate(
            customers
        )
        validated_customers = self.validator.list_validate(
            customers
        )
        results = []
        err_count = 0
        for validator_customer in validated_customers:
            if not validator_customer["validation"]["valid"]:
                err_count += 1
                logger.info(f"检测出不合格客户：{validator_customer['validation']['errors']},剔除后还剩{len(validated_customers) - err_count}个客户")
                continue
            result = self.analyzer.analyze(
                validator_customer["customer"]
            )

            results.append(result)
        self.saver.save(
            results,
            "result.json"
        )