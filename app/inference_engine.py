class InferenceEngine:
    """Метод прямого логического вывода."""

    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def forward_chain(self, facts):
        derived = dict(facts)
        changed = True

        while changed:
            changed = False
            for rule in self.knowledge_base.get_rules():
                conclusion, confidence = rule.evaluate(derived)
                if conclusion is None:
                    continue

                for key, value in conclusion.items():
                    if derived.get(key) != value:
                        derived[key] = value
                        changed = True

        return derived

    def explain(self, facts):
        derived = dict(facts)
        fired_rules = []

        for rule in self.knowledge_base.get_rules():
            conclusion, confidence = rule.evaluate(derived)
            if conclusion is not None:
                fired_rules.append({
                    "rule_id": rule.rule_id,
                    "description": rule.description,
                    "confidence": confidence,
                    "conclusion": conclusion,
                })

        return fired_rules
