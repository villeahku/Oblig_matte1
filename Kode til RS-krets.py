import numpy as np
import matplotlib.pyplot as plt

# Konstantene for kretsen 
R = 200000  # ohm
C = 0.0001  # 100 uF (farad)
V0 = 9  # batterispenning (volt)

# Teoretisk modell for v(t)
def v_teoretisk(t, R, C):
    return V0 * (1 - np.exp(-t / (R * C)))

# Tidsvektor for plottet
t_values = np.linspace(0, 97, 100)  # 0 til 97 sekunder

# Beregn teoretiske verdier
v_values = v_teoretisk(t_values, R, C)

# Plott den teoretiske kurven
plt.plot(t_values, v_values, label="Teoretisk kurve", color="purple")

# Eksempel på målte data
t_malt = [0, 1, 2, 3, 4, 5 , 6, 7, 10, 13, 16, 19,
         21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51,
         54, 57, 60, 67, 74, 81, 89, 97]  # Tidspunkter i sekunder

v_malt = [0, 0.5, 1.0, 1.4, 1.9, 2.3, 2.4, 2.8, 3.7, 4.4, 4.9, 5.6,
          5.9, 6.3, 6.6, 6.9, 7.2, 7.4, 7.7, 7.8, 7.9, 8.1, 8.2, 8.3, 
           8.4, 8.5, 8.6, 8.8, 8.9, 8.9, 9.0]  # Målte spenninger i volt

# Plott målte data
plt.plot(t_malt, v_malt, color="#D5006D", label="Målte data")

# 
plt.xlabel("Tid (s)")
plt.ylabel("Spenning over kondensator (V)")
plt.title("Sammenligning av målt og teoretisk kurve for RC-krets")
plt.legend()
plt.grid(True)

# Vis plottet
plt.show()
