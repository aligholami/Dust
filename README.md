# Visual Question Answering with Stacked Attention Networks

In this project, we will analyze different methods for building a VQA systems. Our goal is to first produce promising results with basic archtiectures and then develop the model to a degree in which **reasoning** is being done at its best possible state.

## Baseline 1

In this section, we initially implement a VQA model with the following characteristics:

1. Extraction of image feature maps with a VGG-16 convolutional architecture.
2. Averaging embedding scores of words in a question.
3. Concatenating image feature maps and averaged embedding scores.
4. Classifying the obtained inputs from step 3 with answers as labels using a multi-layer perceptron.