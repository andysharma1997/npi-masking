from presidio_analyzer import Pattern,PatternRecognizer

class TitleRecoganizer:
    expected_confidence_level = 0.7 # expected confidence level for this recognizer
    
    def __init__(self,supported_entity) -> None:
        self.titles_list = ["sir", "ma'am", "madam", "mr.", "mrs.", "ms.", "miss", "dr.", "professor"]
        self.title_recogizer = PatternRecognizer(supported_entity=supported_entity, deny_list=self.titles_list)
    
    def load(self):
        return self.title_recogizer