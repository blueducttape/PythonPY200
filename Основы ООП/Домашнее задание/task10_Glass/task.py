class Glass:
    def __init__(self, material: str):
        self.material = material

    def get_material(self) -> str:
        """возвращает материал"""
        return self.material


if __name__ == "__main__":
    glass = Glass('стекло')
    print(glass.get_material())

