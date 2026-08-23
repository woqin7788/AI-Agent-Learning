from logger import logger
from customer import Customer
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

        validator_customers = self.validator.list_validate(
            customers
        )

        results = []
        err_count = 0
        for validator_customer in validator_customers:

            # validation = self.validator.validate(
            #     customer
            # )

            if validator_customer["errors"]:
                err_count += 1
                logger.info(f"检测出不合格客户：{validator_customer['errors']}")
                continue

            customer = Customer(
                validator_customer.get("company"),
                validator_customer.get("country"),
                validator_customer.get("email")
            )
            result = self.analyzer.analyze(
                customer
            )

            results.append(result)

        logger.info(f"validation剔除后还剩{len(customers) - err_count}个客户")


        self.saver.save(
            results,
            "result.json"
        )