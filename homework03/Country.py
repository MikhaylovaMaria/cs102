class Country:
    def __init__(self, capital, population):
        self.capital = capital
        self.population = population

    def __str__(self):
        return f"Node({self.capital, self.population})"
