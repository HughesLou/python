import numpy as np

train_x = np.linspace(-1, 1, 100)
print(*train_x.shape)
print(train_x.shape)
tmp = np.random.randn(*train_x.shape)
train_y = 2 * train_x + np.random.randn(*train_x.shape) * 0.33 + 10

print(train_x)
print(tmp)
print(train_y)


