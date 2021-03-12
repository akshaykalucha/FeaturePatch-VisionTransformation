<br />
<p align="center">
  <a href="#">
    <img src="images/StatisticalPatternRecognition.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Pattern Recognition & Computer Vision</h3>
  <p align="center">
    Fine-tuning code and pre-trained models
    <br />
    <a href="https://arxiv.org/pdf/2010.11929.pdf"><strong>Explore the official paper »</strong></a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Code</a>
      <ul>
        <li><a href="#built-with">Built with</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Working & Test</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Statistical pattern recognition, nowadays often known under the term "machine learning", <br />is the key element of modern computer science. Its goal is to find, learn, and recognize patterns in complex data, <br />for example in images, speech, biological pathways, the internet.

* This repo is a gist of implementation of the Vision Transformation which was introduced in the <a href="https://arxiv.org/pdf/2010.11929.pdf">paper</a>: An Image is worth 16x16 words
* This repository is uses Py-Torch implementation availabale <a href="https://github.com/rwightman/pytorch-image-models">here</a>
* The Py-Torch repository has pre-trained weights

The code just a rewrite & straight implementation of the VisionTransformer class, with minor modifications <br /> and simplifications the class function is easier to run & modify for future work to patch and embed images for classification.

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

The raw implementation of code is built using `python3.7.9` & `pip20.0`
* [Python](https://www.python.org/downloads/release/python-379/)
* [Pip](https://pypi.org/project/pip/)


<!-- GETTING STARTED -->
## Getting Started
<div style="text-align:center"><img align="center" src="images/VT.jpg" alt="Logo"></div>


<h3>A quick overview of the architecture</h3>

<p>The Vision Transformer is an image classifier which takes in an image and outputs the class & sub-class prediction, <b>HOWEVER</b>, <br/>it does that <i>without any convolutional layer</i>, <b>INSTEAD</b> it uses the <i>attention layers</i> which is used already in NLTK, that is-an Attention Mechanism is also an attempt to implement the same action of selectively concentrating on a few relevant things, <br/> while ignoring others in deep neural networks, However, in computer vision, convolutional neural networks (CNNs) are still the norm and self-attention just began to slowly creep into the main body of research.</p>

The network is trained in three steps where image is turned in sequence of 1D tokens to use transform architecture:
* Fine-tuning of the global features pretrained by ImageNet & flatten the patches into 1D vectors.
* Mask inference to obtain the cropped images and perform fine-tuning of the local feature. Hereby, the weights in the global features are fixed.
* Concatenating of the global and local feature outputs and fine-tuning of the fusion feature while freezing the weights of the other features.
* The position embeding allows the network to determine what part of the image a specific patch came from.
</br>
</br>
</br>


<div style="text-align:center"><img src="images/attention.jpg" alt="logo">
</br>

<i><small>stand-alone self-attention</small></i>
</div>


</br>
</br>

### Prerequisites

Install the depecdencies before running the `compute.py` file
* pip
  ```sh
  $ pip install -r requirements.txt
  ```