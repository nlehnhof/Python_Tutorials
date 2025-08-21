import  numpy as np
import matplotlib.pyplot as plt

nums = np.random.randint(1, 100, 10)
plt.plot(nums, marker='o')
plt.title('Random Numbers Plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.savefig('random_numbers_plot.png')
plt.show()