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

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

im = Image.open(args["image"])
if im.size == (384, 384):
    print(f"{bcolors.OKGREEN}Running: the image matches the path, running MLP...{bcolors.ENDC}")
else:
    print(f"{bcolors.WARNING}Warning: Image not 384x384, resizing and overriding!-{bcolors.ENDC}")
    resize(args["image"])
    im = Image.open(args["image"])
img = (np.array(im) / 128) - 1
computation(img)