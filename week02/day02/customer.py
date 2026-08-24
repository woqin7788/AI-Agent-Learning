class Customer:

    def __init__(self, company, country, email):

        self.company = company
        self.country = country
        self.email = email


    def get_info(self) -> dict:

        return {
            "company": self.company,
            "country": self.country,
            "email": self.email
        }