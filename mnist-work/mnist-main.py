# Imports
import torch
from torchvision.transforms import ToTensor
import torchvision.datasets as datasets
import torchvision.models as models
from torch.utils.data import DataLoader
import torch.nn as nn
import matplotlib.pyplot as plt
from copy import deepcopy
import time

# Globals
VISUALIZE = False
SHUFFLE = True
BATCH_SIZE = 64
LEARNING_RATE = 0.01
MOMENTUM = REG = 0.001
WEIGHT_DECAY = .001
EPOCHS = 1
WARMUP = 0
STEPS = [6, 8]
MODEL_OUTPUT = "saved/model.pt"

"""
Function - Data Loading and Prep
"""
def prep_data():
    # Download data
    train = datasets.MNIST(root='./data', train=True, download=True, transform=ToTensor())
    test = datasets.MNIST(root='./data', train=False, download=True, transform=ToTensor())
    # Load data into Data Loaders
    train_dataloader = DataLoader(train, batch_size=BATCH_SIZE, shuffle=SHUFFLE)
    test_dataloader = DataLoader(test, batch_size=BATCH_SIZE, shuffle=SHUFFLE)
    return train_dataloader, test_dataloader

def visualize(img, label):
    plt.imshow(img, cmap='gray')
    plt.title("Class : {}".format(label))
    plt.show()

def visualize_data_from_loader(loader):
    train_features, train_labels = next(iter(loader))
    img = train_features[0].squeeze()
    label = train_labels[0]
    visualize(img, label)

"""
Functions - Model/Training Prep
"""
def get_model():
    model = models.efficientnet_b0()
    if torch.cuda.is_available():
        model = model.cuda()
    return model

def get_criterion():
    return nn.CrossEntropyLoss()

def get_optimizer(model):
    return torch.optim.SGD(model.parameters(), LEARNING_RATE,
                                momentum=MOMENTUM,
                                weight_decay=WEIGHT_DECAY)

"""
Functions - Training and Validation
"""
def add_layer_grey_to_color(data):
    conv = nn.Conv2d(1, 3, 1)
    if torch.cuda.is_available():
        conv = conv.cuda()
    multi_channel = conv(data)
    return multi_channel

def change_learning_rate(optimizer, epoch):
    epoch += 1
    if epoch <= WARMUP:
        lr = LEARNING_RATE * epoch / WARMUP
    elif epoch > STEPS[1]:
        lr = LEARNING_RATE * 0.01
    elif epoch > STEPS[0]:
        lr = LEARNING_RATE * 0.1
    else:
        lr = LEARNING_RATE
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr

class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

def accuracy(output, target):
    """Computes the precision@k for the specified values of k"""
    batch_size = target.shape[0]
    _, pred = torch.max(output, dim=-1)
    correct = pred.eq(target).sum() * 1.0
    acc = correct / batch_size
    return acc

def train(epoch, data_loader, model, optimizer, criterion):
    # Record times, losses, accuracy
    iter_time = AverageMeter()
    losses = AverageMeter()
    acc = AverageMeter()
    # For each batch
    for idx, (data, target) in enumerate(data_loader):
        start = time.time()
        # Send to GPU if possible
        if torch.cuda.is_available():
            data = data.cuda()
            target = target.cuda()
        
        multi_channel = add_layer_grey_to_color(data)
        out = model.forward(multi_channel)
        loss = criterion(out, target)
        model.zero_grad()
        loss.backward()
        optimizer.step()

        batch_acc = accuracy(out, target)

        losses.update(loss, out.shape[0])
        acc.update(batch_acc, out.shape[0])

        iter_time.update(time.time() - start)
        if idx % 10 == 0:
            print(('Epoch: [{0}][{1}/{2}]\t'
                   'Time {iter_time.val:.3f} ({iter_time.avg:.3f})\t'
                   'Loss {loss.val:.4f} ({loss.avg:.4f})\t'
                   'Prec @1 {top1.val:.4f} ({top1.avg:.4f})\t')
                   .format(epoch, idx, len(data_loader), iter_time=iter_time, loss=losses, top1=acc))

def validate(epoch, val_loader, model, criterion):
    iter_time = AverageMeter()
    losses = AverageMeter()
    acc = AverageMeter()

    num_class = 10
    cm =torch.zeros(num_class, num_class)
    # evaluation loop
    for idx, (data, target) in enumerate(val_loader):
        start = time.time()

        if torch.cuda.is_available():
            data = data.cuda()
            target = target.cuda()

        with torch.no_grad():
            multi_channel = add_layer_grey_to_color(data)
            out = model.forward(multi_channel)
            loss = criterion(out, target)

        batch_acc = accuracy(out, target)

        # update confusion matrix
        _, preds = torch.max(out, 1)
        for t, p in zip(target.view(-1), preds.view(-1)):
            cm[t.long(), p.long()] += 1

        losses.update(loss, out.shape[0])
        acc.update(batch_acc, out.shape[0])

        iter_time.update(time.time() - start)
        if idx % 10 == 0:
            print(('Epoch: [{0}][{1}/{2}]\t'
               'Time {iter_time.val:.3f} ({iter_time.avg:.3f})\t')
               .format(epoch, idx, len(val_loader), iter_time=iter_time, loss=losses, top1=acc))
    cm = cm / cm.sum(1)
    per_cls_acc = cm.diag().detach().numpy().tolist()
    for i, acc_i in enumerate(per_cls_acc):
        print("Accuracy of Class {}: {:.4f}".format(i, acc_i))

    print("* Prec @1: {top1.avg:.4f}".format(top1=acc))
    return acc.avg, cm

"""
Functions - Model IO
"""
def save_model(model):
    print(f"Saving model to {MODEL_OUTPUT}")
    torch.save(model.state_dict(), MODEL_OUTPUT)

def load_model():
    model = models.efficientnet_b0()
    model.load_state_dict(torch.load(MODEL_OUTPUT))
    model.eval()
    return model

"""
Functions - Main
"""
def main():
    # Data Prep
    train_dataloader, test_dataloader = prep_data()
    if VISUALIZE:
        visualize_data_from_loader(train_dataloader)

    # Augmentation

    # Define import parameters
    model = get_model()
    criterion = get_criterion()
    optimizer = get_optimizer(model)

    # Begin process of training and validation
    best = {"accuracy" : 0, "model" : None, "class_accuracy" : None}
    for epoch in range(EPOCHS):
        change_learning_rate(optimizer, epoch)

        # train loop
        train(epoch, train_dataloader, model, optimizer, criterion)

        # validation loop
        acc, class_accuracy = validate(epoch, test_dataloader, model, criterion)

        if acc > best['accuracy']:
            best = {"accuracy" : acc, "model" : deepcopy(model), "class_accuracy" : class_accuracy}

    # Results
    print('Best Prec @1 Acccuracy: {:.4f}'.format(best['accuracy']))
    per_cls_acc = best['class_accuracy'].diag().detach().numpy().tolist()
    for i, acc_i in enumerate(per_cls_acc):
        print("Accuracy of Class {}: {:.4f}".format(i, acc_i))

    # Save
    save_model(model)
    
# Run main
if __name__ == '__main__':
    main()
