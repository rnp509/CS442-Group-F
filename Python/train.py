import torch
import torch.utils.data
from torch.autograd import Variable
import csv

N, D_in, H, D_out = 10, 2, 10, 1
learning_rate = 1e-2
num_epochs = 25

def get_dataset(filename):
  data = []
  target = []
  with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if (row['open'] and row['close'] and row['previous_day_open']):
        data.append([float(row['open']), float(row['previous_day_open'])])
        target.append([float(row['close'])])
  return torch.utils.data.TensorDataset(torch.Tensor(data), torch.Tensor(target))

def create_model():
  return torch.nn.Sequential(
      torch.nn.Linear(D_in, H),
      torch.nn.ReLU(),
      torch.nn.Linear(H, D_out),
    )

def train(model, dataset):
  dataloader = torch.utils.data.DataLoader(dataset, batch_size=N, shuffle=True)
  loss_fn = torch.nn.MSELoss(size_average=False)
  optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
  for epoch in range(0, num_epochs):
    for batch_id, batch in enumerate(dataloader):
      x = Variable(batch[0])
      y = Variable(batch[1], requires_grad=False)
      y_pred = model(x)
      loss = loss_fn(y_pred, y)
      print(epoch, batch_id, loss.data[0])
      optimizer.zero_grad()
      loss.backward()
      optimizer.step()

if __name__ == "__main__":
  dataset = get_dataset("ethereum.csv")
  model = create_model()
  train(model, dataset)
  torch.save(model, "ethereum.model")

