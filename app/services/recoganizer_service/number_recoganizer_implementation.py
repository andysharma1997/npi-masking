from typing import List
from presidio_analyzer import EntityRecognizer, RecognizerResult
from presidio_analyzer.nlp_engine import NlpArtifacts


class NumbersRecognizer(EntityRecognizer):

    expected_confidence_level = 0.7  # expected confidence level for this recognizer

    def load(self) -> None:
        """No loading is required."""
        pass

    def analyze(
        self, text: str, entities: List[str], nlp_artifacts: NlpArtifacts
    ) -> List[RecognizerResult]:
        """
        Analyzes test to find tokens which represent numbers (either 123 or One Two Three).
        """
        results = []

        # iterate over the spaCy tokens, and call `token.like_num`
        for token in nlp_artifacts.tokens:
            if token.like_num:
                result = RecognizerResult(
                    entity_type="NUMBER",
                    start=token.idx,
                    end=token.idx + len(token),
                    score=self.expected_confidence_level,
                )
                results.append(result)
        return results