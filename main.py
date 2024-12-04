"""
Create a Graph: Initialize the graph structure.
Add Nodes: Insert nodes into the graph.
Add Neighbors to Each Node: Establish connections between nodes by adding neighbors.
Create a Deep Copy of the Graph: Implement functionality to clone the graph using both a cloning method and a copy constructor.
Display the Graph: Present the head nodes of the graph along with their linked neighbors. Include node identification using id(object) as well as their respective values.
Use the @get_node_cache Decorator: Implement caching to reuse existing nodes when adding new nodes, ensuring efficient memory use.

@Author Liad Kashanovsky 4/12/24
liadky@gmail.com
"""

import copy


def get_node_cache(func):
    global node_cache

    def wrapper(*args, **kwargs):
        # print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        node_item: node = kwargs["node_item"]
        node_id: int = id(node_item)
        cache_item = node_cache.get(node_id)
        if cache_item is None:
            node_cache[node_id] = node_item
        else:
            kwargs["node_item"] = cache_item
        result = func(*args, **kwargs)
        # print(f"{func.__name__} returned: {id(result)}")
        return result

    return wrapper


class node(object):
    def __init__(self, value=0):
        self.node_list: set[node] = set()
        self.value = value

    @get_node_cache
    def add(self, *, node_item) -> object:
        self.node_list.add(node_item)
        return node_item

    def __repr__(self):
        if len(self.node_list) == 0:
            return ""

        res: str = "\n Neighbours:"
        for item in self.node_list:
            res += f"\n     id:{id(item)} value: {item.value} "
        return res


node_cache: dict[int, node] = {}


class graph(object):
    """Default and Copy constructor"""
    def __init__(self, graph_item=None):
        self.__graph_set: set[node] = set()
        if graph_item is not None:
            self.__graph_set = copy.deepcopy(graph_item.__graph_set)

    @get_node_cache
    def add(self, *, node_item: node) -> node:
        self.__graph_set.add(node_item)
        return node_item

    def __repr__(self):
        res: str = "Graph:"
        for item in self.__graph_set:
            res += f"\n id:{id(item)} value: {item.value} "
            res += repr(item)
        return res

    def clone(self) -> object:
        if len(self.__graph_set) > 0:
            return copy.deepcopy(self)
        return graph()


if __name__ == '__main__':
    """Create Nodes"""
    node_item1 = node(value=1)
    node_item2 = node(value=2)
    node_item3 = node(value=3)
    node_item4 = node(value=4)

    graph_item: graph = graph()
    """Add nodes 1,2,3,4 to graph"""
    graph_item.add(node_item=node_item1)
    graph_item.add(node_item=node_item2)
    graph_item.add(node_item=node_item3)
    graph_item.add(node_item=node_item4)

    """Add to Node 1 Neighbours, including itself"""
    node_item1.add(node_item=node_item1)
    node_item1.add(node_item=node_item2)
    node_item1.add(node_item=node_item3)
    node_item1.add(node_item=node_item4)

    """Add to Node 3 Neighbours, including itself"""
    node_item3.add(node_item=node_item2)
    node_item3.add(node_item=node_item3)
    print(f"Original Graph")
    print(graph_item)
    graph_item2: graph = graph_item.clone()
    print(f"Cloned Graph graph_item.clone()")
    print(graph_item2)
    graph_item3: graph = graph(graph_item2)
    print(f"Cloned Graph by copy constructor graph(graph_item2)")
    print(graph_item3)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
