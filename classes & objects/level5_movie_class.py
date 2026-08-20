class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def display_info(self):
        print("Title:", self.title)
        print("Director:", self.director)
        print("Year:", self.year)
        print("-------------------------")

movie1 = Movie("Baahubali 2", "S. S. Rajamouli", 2017)
movie2 = Movie("Pushpa: The Rise", "Sukumar", 2021)
movie3 = Movie("Geetha Govindam", "Parasuram", 2018)

movie1.display_info()
movie2.display_info()
movie3.display_info()
