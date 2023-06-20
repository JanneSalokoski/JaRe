import sqlite3

class Database:
	def __init__(self, dbfile):
		self.dbfile = dbfile
		
		self.connect()
		self.cur = self.con.cursor()

		self.tables = {
			"movies": "movie"
		}

	def connect(self):
		self.con = sqlite3.connect(self.dbfile)

	def execute(self, *args):
		print(args)
		res = self.cur.execute(*args)
		return res.fetchall()


	def add_movie(self, title, year, rating):
		self.execute("INSERT INTO movie VALUES (?, ?, ?)", (title, year, rating))

	def get_movies(self):
		return self.execute("SELECT * FROM movie")


class Movies:
	def __init__(self, dbfile):
		self.db = Database(dbfile)
		self.table = "movie"

	def get_movies(self):
		return self.db.execute("SELECT * FROM movie")


DBFILE = "tutorial.db"


def main():
	#db = Database("tutorial.db")
	#movies = db.get_movies()

	movies = Movies(DBFILE)
	res = movies.get_movies()

	print(res)
	






if __name__ == "__main__":
	main()
