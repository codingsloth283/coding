
#notes
print("This is a notes app, the notes will be saved in a txt file in the Directory you are in")
inputnote = input("input a note: ")
title_input = input("input a title: ")
print("Title: "+title_input)
print(inputnote)

with open("notes.txt", "a") as f:
    f.write("Title: "+title_input="\n")
    f.write(inputnote+"\n"
           )




