import torch
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt


x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor), shape=(100, 1)
y = x.pow(2) + 0.2*torch.rand(x.size())
print(x, y)
plt.ion()
plt.scatter(x.data.numpy(), y.data.numpy())
plt.show()
