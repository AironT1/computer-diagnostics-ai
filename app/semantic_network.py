class SemanticNode:
    """Узел семантической сети."""

    def __init__(self, name):
        self.name = name
        self.links = []

    def add_link(self, target, relation):
        self.links.append({"target": target, "relation": relation})


class SemanticNetwork:
    """Семантическая сеть для предметной области."""

    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = SemanticNode(name)
        return self.nodes[name]

    def add_relation(self, source, target, relation):
        source_node = self.add_node(source)
        target_node = self.add_node(target)
        source_node.add_link(target_node.name, relation)

    def get_neighbors(self, node_name):
        node = self.nodes.get(node_name)
        if node is None:
            return []
        return node.links.copy()

    def get_all_nodes(self):
        return list(self.nodes.keys())
