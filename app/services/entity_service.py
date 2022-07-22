from app.utilities import sken_logger

logger = sken_logger.get_logger(__name__)

class Entity:
    def __init__(self) -> None:
        self.supported_entites = ['PERSON', 'CREDIT_CARD', 'EMAIL_ADDRESS', 'IP_ADDRESS', 'PHONE_NUMBER', 'CREDIT_CARD', 'CRYPTO', 'LOCATION', 'NUMBER', 'AADHAAR', 'TITLE',"INDIAN_NAME"]
        self.current_enttites = ['PERSON', 'CREDIT_CARD', 'EMAIL_ADDRESS', 'IP_ADDRESS', 'PHONE_NUMBER', 'CREDIT_CARD', 'CRYPTO', 'LOCATION', 'NUMBER', 'AADHAAR', 'TITLE',"INDIAN_NAME"]
    
    def get_supported_entities(self):
        return self.supported_entites
    
    def get_current_entites(self):
        return self.current_enttites
    
    def remove_entity(self,entity):
        if entity in self.current_enttites:
            self.current_enttites.remove(entity)
            return True
        return False
            
    def add_entity(self,entity):
        if entity not in self.current_enttites and entity in self.get_supported_entities():
            self.current_enttites.append(entity)
            return True
        return False
        