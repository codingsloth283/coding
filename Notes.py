
#notes
print("This is a notes app, the notes will be saved in a txt file in the Directory you are in")
inputyorn = input("type y to input a note and n to not")
if inputyorn == "y":
	
	inputnote = input("input a note: ")
	title_input = input("input a title: ")
	print("Title: "+title_input)
	print("Note: "+inputnote)

	with open("notes.txt", "a") as f:
		f.write("Title: "+title_input+'\n')
		f.write("Note: "+inputnote+'\n')

print("previous notes")
with open("notes.txt") as inp:
	data = set(inp.read().splitlines())
	print(data)

inputclear = input("type clear to clear the notes.txt file")
if inputclear == "clear":
	open('notes.txt', 'w').close()

