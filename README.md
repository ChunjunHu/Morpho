# Morpho - an Open-Source Toolkit for Generative AI from Social Media

Morpho is a set of python tools that allows one to create synthetic data using social media scrapping tools and generative deep learning models such as generative adversarial networks (GANs), variational autoencoders (VAEs) and Diffusion Models to create novel images. Mopho allows one to creating novel images of things like butterfies, sneakers and animals starting with just a keyword list.

The name comes from morpho butterflies, which comprise many species of Neotropical butterfly under the genus Morphoare and are some of the of the most social insects in the animal kingdom.

![image](https://github.com/daydayup-hb-cj/Morpho/blob/main/IMG/BigGANResults.png)

# Lab Environment
**Lab Environment:**
In the Colab environment, the program will automatically install the correct libraries.
```
    Numpy 1.19.1
    Tensorflow 1.14.0
    Keras 2.2.5
    OS: Colab
```
# Dataset and Network
## Dataset
Our dataset has a total of 899 different categories of sneakers, and each category has about 50 to 80 different images, a total of 52,736 images. The dataset we created and used has been published on Kaggle: https://www.kaggle.com/datasets/huchunjun/sneaker899-classificationtotal-50000-images. If the link does not work, please use the alternate link: https://drive.google.com/drive/folders/1bZn-gJ72Lsc0o39HDu4n_RnM_h86yCk-?usp=sharing.

![image](https://github.com/daydayup-hb-cj/Morpho/blob/main/IMG/datasetVisualization.png)

## Network
### Binary Classification

![image](https://github.com/daydayup-hb-cj/Morpho/blob/main/IMG/binaryClassificationStructure.png)

### BigGAN

![image](https://github.com/daydayup-hb-cj/Morpho/blob/main/IMG/networkStructure.png)

# Instruction of binary classification for data cleaning

We use binary classification for data cleaning to obtain a more accurate dataset.

1. Run `sneaker1.jupyter`. First, change workspace path to root path, I have give an example in the `./BigGan/BigGan.jupyter`. Input the right path of your sampled groundTruth dataset.
2. You can get the model in the `predict` dir after training
3. Use the high-precision model to cleaning you whole dataset.
4. **Tips:** we recommed you that run `dataPreprocessing.py` before install your dataset. It can extract pictures in subfolders, convert them to RGB format, and save all pictures in the same folder. In the process, it can delete damaged pictures and skip pictures that cannot be read correctly.

# Instructiion of BigGAN

The code about BigGan, we stored them under the `./BigGan`. This program can realize real-time sampling visualization output, save the trained models of the last 5 epochs, continue training, output tensorboard files and other functions.

1. Import gorundTruth dataset. For example, `./BigGan/dataset/yourDirName`.
```
|-----yourDirName
    |-----xxx.jpg
    |-----xxx.jpg
```
2. Run `BigGan.jupyter`. Remember set right workspace first!!!
3. **Tips:** Under `BigGan.jupyter`, we have integrated the method of calculating FID and some data checking methods to prevent image reading errors. Feel free to use. For the FID method, we need to merge two Python files. Since the current stage is to extract the image and then resize the image, the image pixels will be damaged during the saving process.

# Issues:

1. Update the FID method. Since there will be pixel loss in saving the image, the function should be integrated into BigGan, and the tensor of the images should be input directly.
2. Try LeakyReLU instead of Relu.
3. Retrain the model under large-scale training. Due to the limitation of computing power at this stage, it is impossible to use an excessively large Batch Size and Latent Space.
4. After training to achieve better results, try semi-supervised models and improve BigGAN.

# Reference
[1] Brock, A., Donahue, J., & Simonyan, K. (2018). Large scale GAN training for high fidelity natural image synthesis. arXiv preprint arXiv:1809.11096.<br>
[2] Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., ... & Bengio, Y. (2014). Generative adversarial nets. Advances in neural information processing systems, 27.<br>
[3] Li, H.-T., Yang, W.-H., & Chiang, C.-K. (2020). Outside the box: New style discovering via    Generative Adversarial Network for shoes design. 2020 IEEE International Conference on Consumer Electronics - Taiwan (ICCE-Taiwan). https://doi.org/10.1109/icce-taiwan49838.2020.9258223 <br>
[4] Heusel, M., Ramsauer, H., Unterthiner, T., Nessler, B., & Hochreiter, S. (2017). Gans trained by a two time-scale update rule converge to a local nash equilibrium. Advances in neural information processing systems, 30.<br>
[5] Taki0112 (2019) BigGAN-Tensorflow [Source code]. https://github.com/taki0112/BigGAN-Tensorflow.<br>
[6] Kingma, D. P., Salimans, T., Jozefowicz, R., Chen, X., Sutskever, I., & Welling, M. (2016). Improved variational inference with inverse autoregressive flow. Advances in neural information processing systems, 29.<br>
[7] Salimans, T., Goodfellow, I., Zaremba, W., Cheung, V., Radford, A., & Chen, X. (2016). Improved techniques for training gans. Advances in neural information processing systems, 29.<br>








