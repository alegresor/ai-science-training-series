import numpy as np
from matplotlib import pyplot

for n in [1,2,4,8]:
    x = np.loadtxt('./metrics/metrics_n%d.dat'%n) # train_acc, train_loss, valid_acc, valid_loss, time_per_epochs
    fig,ax = pyplot.subplots()#nrows=1,ncols=1,figsize=(4,4))
    ax.plot(x[:,0],color='c',label='training')
    ax.plot(x[:,2],color='m',label='validation')
    ax.legend()
    ax.set_xlabel('epochs')
    ax.set_ylabel('accuracy')
    fig.savefig('./accuracy_%d.pdf'%n)