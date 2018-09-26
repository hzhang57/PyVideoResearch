"""
Temporal Segment Networks
from
Temporal Segment Networks: Towrads Good Practices for Deep Action Recognition
Liming Wang et al.
"""
import torch.nn as nn
from wrapper import Wrapper


class TSNBase2(Wrapper):
    def __init__(self, basenet, args):
        self.consensus = lambda x: x.mean(1)
        super(TSNBase2, self).__init__()

    def forward(self, x):
        # input is b, t, ...
        s = x.shape
        b, t = s[0], s[1]
        x = x.reshape(-1, *s[2:])
        out = self.basenet(x)
        out = out.reshape(b, t, *out.shape[1:])
        #return self.consensus(out)
        return out.permute(0, 2, 1)
