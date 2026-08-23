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

        results = []

        for customer in customers:

            validation = self.validator.validate(
                customer
            )

            if not validation["valid"]:
                continue

            result = self.analyzer.analyze(
                customer
            )

            results.append(result)

        self.saver.save(
            results,
            "result.json"
        )