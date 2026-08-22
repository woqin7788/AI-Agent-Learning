from customer import Customer
import re

from logger import logger


class CustomerValidator:
    def validate_email(self, email: str) -> bool:
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        return re.match(pattern, email) is not None

    def validate(self,customer:Customer)->dict:
        errors=[]
        if not customer.company:
            errors.append("公司名称为空")
        if not customer.country:
            errors.append("国家为空")
        if not customer.email:
            errors.append("邮箱为空")
        elif  not self.validate_email(customer.email):
            errors.append("邮箱格式错误")
        if errors:
            return {
                "valid": False,
                "reason": errors
            }

        return {
                "valid": True,
                "reason": ""
            }
