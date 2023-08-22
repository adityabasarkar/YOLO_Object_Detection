import torch#, cv2, os, random, json, time, sys
from torch.autograd import Variable
# import numpy as np
# import torch.nn as nn
# import torch.optim as optim
# from torchvision import models, transforms
# from torchvision.models.vgg import VGG16_Weights
# from torchsummary import summary
# import torchvision.datasets as datasets
# from torch.utils.data import DataLoader, Dataset
# from PIL import Image
# import VideoCapture as vc
# import albumentations as alb

x = Variable(torch.tensor([3.0]), requires_grad=True)

y = 4 * (x + 1) ** 3

y.backward()
print(x.grad)