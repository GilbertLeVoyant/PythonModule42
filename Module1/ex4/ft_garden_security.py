class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        if height > 0:
            self._height = height
        else:
            print(f"Invalid operation attempted: height {height} [REJECTED]")
            print("Security: Negative height rejected")
        if age > 0:
            self._ages = age
        else:
            print(f"Invalid operation attempted: age {age} [REJECTED]")
            print("Security: Negative age rejected")

    def set_height(self, height: int):
        if height > 0:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height} [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int):
        if age > 0:
            self._ages = age
            print(f"Age updated: {self._ages} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self):
        return self._ages

    def get_height(self):
        return self._height


# if __name__ == "__main__":
#    print("=== Garden Security System ===")
#    p = SecurePlant("Rose", 20, 15)
#    print(f"Plant created: {p.name}")
#    p.set_height(25)
#    p.set_age(30)

#    p.set_height(-5)
#    print(f"\nCurrent p: {p.name} ({p.get_height()}cm, {p.get_age()} days)")
