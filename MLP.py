import torch
import torch.nn as nn

class MLP(nn.Module):
    """Multilayer perceptron.
    Parameters: in_features, hidden_features, out_features, p
    Attributes: fc, act, fc2, drop
    """

    def __init__(self, in_features, hidden_features, out_features, p=0.):
        super().__init__()
        self.fc1 = nn.Linear(in_features, hidden_features)
        self.act = nn.GELU()
        self.fc2 = nn.Linear(hidden_features, out_features)
        self.drop = nn.Dropout(p)
    
    def forward(self, x):
        """Run forward pass.
        Parameters: x
        Returns: torch.Tensor
        """
        x = self.fc1(
                x
        )
        x = self.act(x)
        x = self.drop(x)
        x = self.fc2(x)
        x = self.drop(x)

        return x
