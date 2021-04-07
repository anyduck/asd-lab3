from typing import Optional


class ColoredGraph:
    def __init__(self, incidence_matrix: list[list]):
        self._matrix = incidence_matrix
        self._nodes = len(self._matrix)
        self._colors = [None] * self._nodes
        self._chromatic_number = self._get_chromatic_number()

    @property
    def chromatic_number(self):
        return self._chromatic_number


    def _is_colored(self) -> bool:
        """ Поеревіряє чи розфарбований граф. """

        return self._colors.count(None) == 0


    def _get_chromatic_number(self) -> int:
        """ Повертає хроматичне число графу. """

        if self._is_colored():
            return len(set(self._colors))
        return max(row.count(1) for row in self._matrix)


    def _get_possible_colors(self, node: int) -> set[int]:
        """ Повертає можливі кольори вершини. """

        if self._colors[node] is not None:
            return set()

        colors = set(range(self._chromatic_number))
        for neighbor, is_incident in enumerate(self._matrix[node]):
            if is_incident and self._colors[neighbor] in colors:
                colors.remove(self._colors[neighbor])

        return colors


    def _get_next_node_and_colors(self) -> tuple[Optional[int], set[int]]:
        """ Евристична функція MVR для розфарбування графу. """

        possible_colors = [set() for _ in range(self._nodes)]
        next_node, next_colors = None, set(range(self._chromatic_number + 1))

        for node in range(self._nodes):
            if self._colors[node] is None: 
                colors = self._get_possible_colors(node)
                possible_colors[node] = colors
                if len(colors) < len(next_colors):
                    next_node, next_colors = node, colors

        return next_node, next_colors


    def _find_colors(self) -> bool:
        """ Знаходить кольори вершин рекрсивним пошуком з поверненням.
        
        Повертає True, якщо граф розфарбовано. """

        if self._is_colored():
            return True

        node, colors = self._get_next_node_and_colors()

        if node is None or not colors:
            return False

        for color in colors:
            self._colors[node] = color
            if self._find_colors():
                return True
        self._colors[node] = None


    def get_colors(self):
        """ Повертає кольори вершин розфарбованого графу. """

        self._find_colors()
        self._chromatic_number = self._get_chromatic_number()

        return self._colors
