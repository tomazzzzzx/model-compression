import torch

class MagnitudePruner:
    def __init__(self, sparsity=0.5): self.sp = sparsity
    def prune(self, model):
        for n, p in model.named_parameters():
            if "weight" in n:
                t = torch.quantile(p.data.abs().flatten(), self.sp)
                p.data *= (p.data.abs() >= t)
        return model
