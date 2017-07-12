import numpy as np

class Candidate():
    """Represents a single candidate in a single generation"""
    def __init__(self, dup=None, parent=None):
        self.nodes = []
        self.links = []
        # Handle duplication of candidate from previous generation
        if dup:
            pass
        # Handle transformation of candidate from previous generation
        elif parent:
            pass
        # Handle brand new candidates
        else:
            node_count = np.random.randint(4, 9)
            for _ in range(node_count):
                node = {'position': np.random.rand(2), 'friction': np.random.rand()}
                self.nodes.append(node)
            self.__set_links()
    
    def __set_links(self):
        """Define the links for this candidate"""
        self.__set_initial_links()
        self.__set_extra_links()
    
    def __set_initial_links(self):
        """
            Define the initial tree for this candidate - this ensures a full
            network of links and a single organism
        """
        disconnected_nodes = list(range(len(self.nodes)))
        connected_nodes = []
        while disconnected_nodes:
            node1 = disconnected_nodes.pop()
            if connected_nodes:
                node2 = np.random.choice(connected_nodes, size=1)
            else:
                node2 = np.random.choice(disconnected_nodes, size=1)
                disconnected_nodes.remove(node2)
            link_power = np.random.random() + 0.5
            ideal_length = np.random.random() * 0.95 + 0.05
            link = {'nodes': [node1, node2], 'power': link_power, 'ideal_length':           ideal_length}
            self.links.append(link)
            connected_nodes.append(node1)
            if not node2 in connected_nodes:
                connected_nodes.append(node2)
    
    def __set_extra_links(self):
        """Add additional links to distinguish this candidate"""
        node_table = [[1] * len(self.nodes)] * len(self.nodes)
        for i in range(len(self.nodes)):
            node_table[i][i] = 0
        for link in self.links:
            x, y = link['nodes']
            node_table[x][y] = node_table[y][x] = 0
        for _ in range(np.random.randint(1, self.node_count * 2)):
            available_links = self.__available(node_table)
            if available_links:
                new_link_nodes = np.random.choice(available_links)
                link = {'nodes': new_link_nodes, 'power': np.random.random() + 0.5,
                        'ideal_length': np.random.random() * 0.95 + 0.05}
                a, b = new_link_nodes
                node_table[a][b] = node_table[b][a] = 0
            else:
                # There are no possible links to add, so stop adding links
                break
    
    def __available(self, node_table):
        """
            Determine whether or not there are any available links
            as represented in node_table
        """
        result = []
        for i in range(len(node_table)):
            for j in range(i):
                if node_table[i][j]:
                    result.append([i, j])
        return result
