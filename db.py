import sqlite3 as sqlite
import json
from json import JSONEncoder

DB_NAME = "test.db"

class Roommate:
	def __init__(self, name, stats):
		self.name = name
		self.stats = stats
	def __repr__(self):
		return "<Roommate name: %s, stats: %s>" % (self.name, str(self.stats))
	def __str__(self):
		return "%s: %s" % (self.name, str(self.stats))
	def to_dict(self):
		return {"name": self.name, "stats": [o.to_dict() for o in self.stats]}

class Stat:
	def __init__(self, stat, amount):
		self.stat = stat
		self.amount = amount
	def __repr__(self):
		return "<Stat: %s, amount: %s>" % (self.stat, self.amount)
	def to_dict(self):
		return {"stat": self.stat, "amount": self.amount}

def main():
	#print(get_all_names())
	#print(get_stats_for_name("kyle"))
	#print(get_all_stats())
	print(get_all())

def connect():
	connection = sqlite.connect(DB_NAME)
	return connection

def get_all():
	conn = connect()
	conn.text_factory = str
	c = conn.cursor()
	names = []
	stats = []
	roommate_list = []

	c.execute("select * from loadz")
	rows = c.fetchall()

	for row in rows:
		if row[1] not in names:
			names.append(row[1])

	for name in names:
		roommate_list.append(Roommate(name, []))


	for roommate in roommate_list:
		for row in rows:
			if roommate.name == row[1]:
				roommate.stats.append(Stat(row[2], row[3]))

	results = [obj.to_dict() for obj in roommate_list]
	jsdata = json.dumps({"roommates": sorted(results)})
	return jsdata

def get_stats_for_name(name):
	roommates = get_all()
	return [r.stats for r in roommates if r.name == name][0]

def increase_count(name, stat):
	conn = connect()
	c = conn.cursor()

	c.execute("update loadz set amount = amount + 1 where name=? and stat=?", (name, stat))
	conn.commit()
	conn.close()

def decrease_count(name, stat):
	conn = connect()
	c = conn.cursor()

	c.execute("update loadz set amount = amount - 1 where name=? and stat=?", (name, stat))
	conn.commit()
	conn.close()

if __name__ == "__main__":
	main()
