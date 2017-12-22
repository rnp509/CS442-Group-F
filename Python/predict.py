import sys
import torch
from torch.autograd import Variable

if __name__ == "__main__":
  if len(sys.argv) < 4:
    print("Not enough parameters!\nUsage: {} <model> <open> <previous day open>".format(sys.argv[0]))
    sys.exit()
  model = torch.load(sys.argv[1])
  measurement = Variable(torch.Tensor([[float(sys.argv[2]), float(sys.argv[3])]]))
  prediction = model(measurement)
  print(prediction)

