from dataclasses import dataclass,field

@dataclass
class Customer:
    company: str
    country: str
    email: str | None = None
    tags: list[str] = field(default_factory=list)

    def get_info(self):
        # 将 Customer 对象转换成字典
        return {
            "company": self.company,
            "email": self.email,
            "country": self.country,
            "tags": self.tags
        }