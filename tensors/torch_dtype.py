import torch
import numpy as np

#  тензоры торча работают примерно как в нампае. Принимают тензоры в первую очередь размер
x = torch.empty(2, 2)
print(x)

#  различные операции инициализации тензоров
x = torch.ones(2, 2)
print(x)

x = torch.zeros(2, 2)
print(x)

x = torch.rand(2, 2)  # от 0 до 1
print(x)

# работа с типом данных торча
x = torch.rand(2, 2, dtype=torch.float)
print(x)
print(x.dtype)
print(x.size())  # размер тензора (если забыли))

a = [[1, 2, 3], [3, 4, 5]]
np_a = np.array(a)
torch_a = torch.tensor(np_a)
print(torch_a)
print(torch_a.size())  # работа с нампаем


# сложение и произведение торчей аналогично нампаю
b = torch.rand(2, 3)
c = torch_a + b  # out of place
print(c)
# b.add_(torch_a)  # in place (в принципе, все операции через нижнее подчеркивание в конце у торча делают in place edit)
# print(b)

# аналогично разность и произведение

c = torch_a - b == torch.sub(torch_a, b)  # в результате сравнения в торче получается не бул объект, а массив из булов
print(c)
c = torch_a * b
print(c)
c = torch_a / b
print(c)
c = torch_a / torch.zeros(2, 3)  # бесконечности, никакого ZeroDivision
print(c)
