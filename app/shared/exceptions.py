class ServiceNotAvaliableError(Exception):
    def __init__(self, message="Service not avaliable"):
        self.message = message
        super().__init__(self.message)

class EmailNotFound(Exception):
    def __init__(self, message="Email not found"):
        self.message = message
        super().__init__(self.message)


class CampaignNotFound(Exception):
    def __init__(self, message="Campaign not found"):
        self.message = message
        super().__init__(self.message)


class RecipientNotFound(Exception):
    def __init__(self, message="Recipient not found"):
        self.message = message
        super().__init__(self.message)


