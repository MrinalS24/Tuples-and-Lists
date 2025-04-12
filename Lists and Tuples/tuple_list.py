fav_songs = ["Fearless", "Getaway Car", "Lover", "All too Well", "Speak Now", "Mean", "Anti-Hero", "Shake it Off","Welcome to New York"]
print(fav_songs)

print()

fav_songs.append("Better Than Revenge")
print(fav_songs)

print()

fav_songs.remove("Fearless")
print(fav_songs)

print()

for songs in fav_songs:
    print("My favorite song is ", songs)


print()


print(fav_songs[0])

print()

length = len(fav_songs)
print(length)

print()

print(fav_songs[-1])

print()

print(fav_songs[-2])

print()

#slicing a list
print(fav_songs)
print(fav_songs[4:9])
print(fav_songs[-5:])
print(fav_songs[:5])

print(end ="\n\n\n")

#2-D Lists
flowers = [["Roses","Pink"],["Marigolds","Yellow"],["Lavender","Purple"],["Baby Blooms","White"]]
print(flowers[2][0])

rows = len(flowers)
print(rows)
print()

column = len(flowers[0])
print(column)

print()

for flower in flowers:
    for item in flower:
        print(item)

print()





#Tuples
sample = (2,8,56,108)

for i in sample:
    print(i)

print()

print(sample[2])

print()

print(sample[-3:])

#sample.append(23) - Once a tuple is made, it is not possible to add data to it.

#sample[0] = 200 - Once a tuple is made, it is not possible to modify data

#sample.remove(2) - Once a tuple is made, it is not possibel to remove data  








