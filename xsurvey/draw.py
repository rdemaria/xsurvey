import matplotlib.pyplot as plt


class Canvas2d:
    def __init__(self, projection="xy", backend="matplotlib"):
        self.projection = projection
        self.entities = set()
        self.style = {}
        if backend != "matplotlib":
            raise NotImplementedError

    def add(self, entity):
        self.entities.add(entity)
        self.update()

    def get_xy(self, position):
        cc = {"x": 0, "y": 1, "z": 2}
        return position[cc[projection[0]], cc[projection[1]]]

    def get_style(self, primi):
        style = self.style
        style.update(style.get(primi.__class__.__name__, {}))
        if hasattr(primi, "layer"):
            style.update(self.style.get(pp.layer, {}))
            style.update(style.get(primi.__class__.__name__, {}))
        if hasattr(primi, "name"):
            style.update(self.style.get(pp.name, {}))
            style.update(style.get(primi.__class__.__name__, {}))
        if hasattr(primi, "style"):
            style.update(pp.style)
            style.update(style.get(primi.__class__.__name__, {}))
        return style

    def update(self):
        self.fig = plt.figure(id(self))
        self.fig.clf()
        self.ax = self.fig.gca()

        primitives = []
        for ee in self.entities:
            primi.extend(ee.render())

        for pp in primitives:
            if isinstance(pp, Point):
                style = self.get_style(pp)
                x, y = self.get_xy(pp.position)
                color = style.get("color", "k")
                markerstyle = style.get("markerstyle", "o")
                ax.plot([x], [y], color=color, markerstyle=markerstyle)
