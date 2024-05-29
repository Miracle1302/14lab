import numpy as np
import matplotlib.pyplot as plt

# Визначаємо функцію Y(x)
def Y(x):
    # Оскільки ми не можемо ділити на нуль, потрібно обробити випадок x=0 окремо
    return np.sin(10*x) * np.sin(3*x) / (x**2) if x != 0 else 0

# Створюємо масив значень x з невеликим кроком для гладкості графіка
x_values = np.linspace(0.01, 4, 400)  # починаємо з 0.01 для уникнення ділення на нуль
y_values = np.vectorize(Y)(x_values)  # векторизуємо функцію Y та обчислюємо y для кожного x

# Створення графіка
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label='Y(x) = sin(10*x)*sin(3*x)/(x^2)', color='blue', linewidth=2)

# Налаштування графіка
plt.title('Graph of the Function Y(x) = sin(10*x)*sin(3*x)/(x^2)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.axhline(0, color='black',linewidth=0.5)  # ось X
plt.axvline(0, color='black',linewidth=0.5)  # ось Y
plt.grid(True)
plt.legend()

# Показуємо графік
plt.show()

