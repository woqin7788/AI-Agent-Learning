from customer import Customer
import re
from logger import logger
from config_loader import ConfigLoader


class CustomerValidator:
    def __init__(self, config: dict):
        self.config = config
    def validate_company(self, customer: Customer) -> str | None:

        if not customer.company:
            return "公司名称为空"

        return None


    def validate_country(self, customer: Customer) -> str | None:

        if not customer.country:
            return "国家为空"

        return None

    def validate_email(self, customer: Customer) -> str | None:

        if not customer.email:
            return "邮箱为空"

        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        if re.match(pattern, customer.email) is None:
            return "邮箱格式错误"

        return None

    def validate(self, customer: Customer) -> dict:

        errors = []
        validators_map = {
            "company": self.validate_company,
            "country": self.validate_country,
            "email": self.validate_email
        }
        rules = self.config["validation_rules"]

        for rule in rules:
            validator = validators_map.get(rule)
            if validator is None:
                logger.warning(f"未知的校验规则: {rule}")
                continue
            error = validator(customer)
            if error:
                errors.append(error)

        return {
            "valid": len(errors) == 0,
            "errors": errors
        }