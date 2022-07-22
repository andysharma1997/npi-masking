from presidio_anonymizer import AnonymizerEngine
from presidio_analyzer import AnalyzerEngine
from typing import List
from concurrent.futures import ProcessPoolExecutor
import os
from app.utilities import sken_logger

logger = sken_logger.get_logger(__name__)

class Anomizer:
    def __init__(self,recoganizers:List) -> None:
        self.recoganizers = recoganizers
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()
        self.language = "en"
    
    def initialize(self):
        logger.info(f"Initializing Base Anomizer with {len(self.recoganizers)} recoganizers")
        for recoganizer in self.recoganizers:
            self.analyzer.registry.add_recognizer(recoganizer)
    
    def anonymize_text(self,sentence,entities):
        ents = self.analyzer.analyze(sentence,language=self.language,entities=entities)
        result = self.anonymizer.anonymize(sentence,analyzer_results=ents)
        return result.text

    def batch_anonymize(self,sentences,entities):
        result = []
        for item in sentences:
            resp = self.anonymize_text(item.lower(),entities)
            result.append({"orignal_sentence": item,"anonymized_sentence":resp})
        return result