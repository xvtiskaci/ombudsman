from elements.element import Element


class BaseForm:

    def __init__(self, by, locator, name):
        self.element = Element(by, locator, name)

    def is_visible(self):
        return self.element.is_visible()
