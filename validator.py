from customer import Customer
import re
from logger import logger


class CustomerValidator:
    def __init__(self, config: dict):
        self.config = config
    #校验客户公司信息，给出错误信息
    def validate_company(self, customer: Customer) -> str | None:

        if not customer.company:
            return "公司名称为空"

        return None

    # 校验客户国家信息，给出错误信息
    def validate_country(self, customer: Customer) -> str | None:

        if not customer.country:
            return "国家为空"

        return None

    # 校验客户邮箱信息，给出错误信息
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

    def list_validate(self, customers: list[Customer]) -> list:
        result = []
        for customer in customers:
            validation_result = self.validate(customer)
            result.append({
                "customer": customer,
                "validation": validation_result
            })
        return result