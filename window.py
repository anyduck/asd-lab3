import contextily
import geopandas
import matplotlib.pyplot


COLORS = ['#009392', '#E9E29C', '#CF597E', '#9CCB86', '#39B185', '#EEB479', '#E88471']
STYLE = dict(edgecolor='black', linewidth=0.3, alpha=0.5)

class Window:
    def __init__(self, shapefile: str):
        self._data = geopandas.read_file(shapefile).set_crs(epsg=3857)
        self._fig, self._ax = matplotlib.pyplot.subplots()
        matplotlib.pyplot.ion()

    def pause(self, delay: float) -> None:
        """ Запускає GUI цикл подій на *delay* секунд. """

        matplotlib.pyplot.pause(delay)

    def draw(self, colors: list[int]) -> None:
        """ Виводить розфарбований граф. """

        self._ax.clear()
        matplotlib.pyplot.tight_layout(pad=0)
        for province, color in enumerate(colors):
            color_ = 'white' if color is None else COLORS[color]
            self._data.loc[[province], 'geometry'].plot(ax=self._ax, color=color_, **STYLE)

        contextily.add_basemap(ax=self._ax, source=contextily.providers.CartoDB.Positron)
        self._ax.axis('off')

    def blank(self) -> None:
        """ Вивидодить пустий граф. """

        self.draw([None] * len(self._data))
        self.pause(1)
