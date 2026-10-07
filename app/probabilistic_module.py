class ProbabilisticModule:
    """Простой вероятностный модуль для оценки возможных диагнозов."""

    def __init__(self):
        self.weights = {}

    def add_weight(self, key, value):
        self.weights[key] = max(0.0, min(1.0, float(value)))

    def estimate(self, facts):
        if not facts:
            return 0.0

        score = 0.0
        count = 0

        for key, value in facts.items():
            if key in self.weights:
                weight = self.weights[key]
                if value is True:
                    score += weight
                elif value is False:
                    score += (1.0 - weight)
                count += 1

        if count == 0:
            return 0.0

        return max(0.0, min(1.0, score / count))
