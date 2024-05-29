import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
data = pd.read_csv('data.csv')

# Створення графіка
plt.figure(figsize=(10, 5))
plt.plot(data['Year'], data['Ukraine'], label='Ukraine', marker='o')
plt.plot(data['Year'], data['Germany'], label='Germany', marker='o')

# Налаштування графіка
plt.title('Population Dynamics: Ukraine vs Germany (2019-2023)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Показ графіка
plt.show()

