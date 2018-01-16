import matplotlib.pyplot as plt

listx = []
listy = []

with open("testFile.csv") as f:
    data = f.readlines()

    print(data[1:1000])

    for i in range(0, 1000):
        listx.append(data[i].split(", ")[0])



# for value in listx:
#     print(value, end="\n")

plt.plot(listx)
plt.show()
