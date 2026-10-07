import json

from app.expert_system import ExpertSystem


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_system_from_data():
    system = ExpertSystem()

    facts_data = load_json("data/facts.json")
    concepts_data = load_json("data/concepts.json")
    rules_data = load_json("data/rules.json")

    for key, value in facts_data["facts"].items():
        system.add_fact(key, value)

    for name, description in concepts_data.items():
        system.add_concept(name, description)

    for rule_data in rules_data:
        system.add_rule(
            conditions=rule_data["conditions"],
            conclusion=rule_data["conclusion"],
            confidence=rule_data["confidence"],
            rule_id=rule_data["rule_id"],
            description=rule_data["description"],
        )

    return system


if __name__ == "__main__":
    system = build_system_from_data()

    result = system.diagnose({
        "power_on": True,
        "no_image": True,
        "monitor_on": True,
        "network_error": False,
        "slow_work": False,
    })

    print("Диагностика:")
    print(json.dumps(result, ensure_ascii=False, indent=2))
