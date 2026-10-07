from app.inference_engine import InferenceEngine
from app.knowledge_base import KnowledgeBase
from app.probabilistic_module import ProbabilisticModule
from app.semantic_network import SemanticNetwork
from app.rules import Rule


class ExpertSystem:
    """Главный класс экспертной системы."""

    def __init__(self):
        self.kb = KnowledgeBase()
        self.engine = InferenceEngine(self.kb)
        self.network = SemanticNetwork()
        self.probabilities = ProbabilisticModule()

    def add_fact(self, key, value):
        self.kb.add_fact(key, value)

    def add_rule(self, conditions, conclusion, confidence=1.0, rule_id=None, description=""):
        if rule_id is None:
            rule_id = f"rule_{len(self.kb.get_rules()) + 1}"

        rule = Rule(
            rule_id=rule_id,
            conditions=conditions,
            conclusion=conclusion,
            confidence=confidence,
            description=description,
        )
        self.kb.add_rule(rule)

    def add_concept(self, name, description=""):
        self.kb.add_concept(name, description)

    def add_relation(self, source, target, relation):
        self.network.add_relation(source, target, relation)

    def add_probability(self, key, value):
        self.probabilities.add_weight(key, value)

    def diagnose(self, symptoms):
        base_facts = dict(symptoms)
        derived_facts = self.engine.forward_chain(base_facts)

        if "check" in derived_facts:
            diagnostic_steps = [derived_facts["check"]]
        else:
            diagnostic_steps = []

        for key, value in derived_facts.items():
            if key.startswith("check") and isinstance(value, str):
                diagnostic_steps.append(value)

        confidence = self.probabilities.estimate(derived_facts)

        result = {
            "symptoms": base_facts,
            "derived_facts": derived_facts,
            "diagnostic_steps": diagnostic_steps,
            "confidence": round(confidence, 2),
        }

        return result
