from turtle import Turtle,Screen
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon",["pikachu","chinnu","anu"])
table.add_column("Type",["electric","fire","cold"])
print(table)