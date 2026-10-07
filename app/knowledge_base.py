class KnowledgeBase:
    """Хранилище фактов, правил и понятий."""

    def __init__(self):
        self.facts = {}
        self.rules = []
        self.concepts = {}

    def add_fact(self, key, value):
        self.facts[key] = value

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_concept(self, name, description=""):
        self.concepts[name] = description

    def get_facts(self):
        return self.facts.copy()

    def get_rules(self):
        return list(self.rules)

    def get_concepts(self):
        return self.concepts.copy()

    def load_from_json(self, facts_data=None, rules_data=None, concepts_data=None):
        if facts_data:
            for key, value in facts_data.items():
                self.facts[key] = value

        if rules_data:
            for rule in rules_data:
                self.rules.append(rule)

        if concepts_data:
            for name, description in concepts_data.items():
                self.concepts[name] = description
