class Song:
  
  def __init__(self, title = "", author = "", lyrics = ()):
    self.title=title 
    self.author=author 
    self.lyrics=lyrics 
    print(f"New song made: {self.title=},{self.author=},{self.lyrics=}")

  def sing(self):
    print(f"A new song made: \n {self.title} - {self.author}")
    print("{}".format(", \n".join(self.lyrics)))

  def yell(self):
    list(self.lyrics)
    self.lyrics = [letter.upper() for letter in self.lyrics]
    print(type(self.lyrics))
    print(*self.lyrics,sep='\n')



ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
#ziemelmeita.sing()
ziemelmeita.yell()
baigais = Song("Baigais džeks", "Super garīgais!", ["Es esmu baigi labais džeks", "Un baigi labais nodoms mans"])
baigais.sing()
baigais.yell()

