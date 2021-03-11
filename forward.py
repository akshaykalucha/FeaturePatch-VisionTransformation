import numpy as np
from PIL import Image
import torch
from resize import resize
import argparse
import os, sys

k = 10
ap = argparse.ArgumentParser()

imagenet_labels = dict(enumerate(open("classes.txt")))
model = torch.load("model.pth")
model.eval()


def computation(image):
    inp = torch.from_numpy(img).permute(2, 0, 1).unsqueeze(0).to(torch.float32)
    logits = model(inp)
    probs = torch.nn.functional.softmax(logits, dim=-1)

    top_probs, top_ixs = probs[0].topk(k)

    for i, (ix_, prob_) in enumerate(zip(top_ixs, top_probs)):
        ix = ix_.item()
        prob = prob_.item()
        cls = imagenet_labels[ix].strip()
        print(f"{i}: {cls:<45} --- {prob:.4f}")


ap.add_argument("-i", "--image", required=True,
	help="name of the image in base dir")
args = vars(ap.parse_args())

