class Rule:
    """Продукционное правило: IF conditions THEN conclusion."""

    def __init__(self, rule_id, conditions, conclusion, confidence=1.0, description=""):
        self.rule_id = rule_id
        self.conditions = conditions or {}
        self.conclusion = conclusion or {}
        self.confidence = confidence
        self.description = description

    def matches(self, facts):
        for key, expected_value in self.conditions.items():
            if facts.get(key) != expected_value:
                return False
        return True

    def evaluate(self, facts):
        if self.matches(facts):
            return self.conclusion, self.confidence
        return None, 0.0
