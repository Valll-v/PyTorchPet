import torch
import numpy as np

x = torch.rand(4, 4)
print(x)
y = x.view(2, 8)
print(y)
y = x.view(-1, 8)
print(y)


a = torch.ones(5)
print(a)
b = a.numpy()
print(b)
print(type(b))  # НО! a и b обращаются к одним ячейкам памяти

a += 1
print(a)
print(b)


np_a = np.array([[1, 2, 3], [3, 4, 5]])
torch_a = torch.tensor(np_a)  # out of place
torch_b = torch.from_numpy(np_a)  # in place (как c a и b выше)
