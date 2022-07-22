from presidio_analyzer import Pattern,PatternRecognizer

class AdharRecoganizer:
    expected_confidence_level = 0.9 # expected confidence level for this recognizer
    
    def __init__(self,supported_entity) -> None:
        self.adhar_pattern =  Pattern(name="adhar_pattern",regex="\d{12}", score = self.expected_confidence_level)
        self.adhar_recogizer = PatternRecognizer(supported_entity=supported_entity,patterns = [self.adhar_pattern])
    def load(self):
        return self.adhar_recogizer