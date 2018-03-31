books = {
		"Harry Potter" : "J.K Rowling",
		"The Fault in Our Stars" : "John Green",
		"The Hunger Games" : "Suzanne Collins",
		"Divergent" : "Veronica Roth",
		"Thirteen Reasons Why" : "Jay Asher",
		"Percy Jackson" : "Rick Riordan",
        "Throne of Glass" : "Sarah J. Maas",
        "Red Queen" : "Victoria Aveyard",
        "City of Bones" : "Cassandra Clare",
        "The Hobbit" : "J.R.R Tolkien"

	}
#prints all keys and values of the dictionary
for key,val in books.items():
    print (key, ">>", val)

#adds elements in the dictionary
books['To Kill a Mockingbird'] = 'Harper Lee'
books['The Book Thief'] = 'Markus Zusak'
books['Ready Player One'] = 'Ernest Cline'

print ("-"*10)

#sorts elements in the dictionary
for key, value in sorted(books.items()):
    print (key,">>", value)


