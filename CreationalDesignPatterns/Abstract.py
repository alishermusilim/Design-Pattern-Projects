class ModernFactory:
    def create_chair(self):
        return "Modern Chair"

    def create_sofa(self):
        return "Modern Sofa"


class VictorianFactory:
    def create_chair(self):
        return "Victorian Chair"

    def create_sofa(self):
        return "Victorian Sofa"


# Usage
factory = ModernFactory()
print(factory.create_chair())
print(factory.create_sofa())