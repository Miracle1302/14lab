import matplotlib.pyplot as plt


labels = 'Boys', 'Girls'
sizes = [14, 9]


colors = ['lightblue', 'lightcoral']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)

ax1.axis('equal')

plt.title('Gender Distribution in a Class')

plt.show()
