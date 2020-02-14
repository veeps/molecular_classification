# Molecular Cell Classification
*Acknowledgments: This project is inspired by the work done in the article, [Learning Drug Functions from Chemical Structures with Convolutional Neural Networks and Random Forests](https://pubs.acs.org/doi/10.1021/acs.jcim.9b00236) by Jesse G Meyer, Shengchao Liu, Ian J Miller, Joshua J Coon, Anthony Gitter Journal of Chemical Information and Modeling. 2019, 59(10) 4438-4449. Their github and data sources can be found [here.](https://github.com/jgmeyerucsd/drug-class)*

## Executive Summary
Using images of molecular chemical structures, I built a multi-class classification model to predict the drug treatment class of the chemical.

---

## Problem Statement
Neglected diseases is a term used to describe diseases that affect a niche population with little to no treatments available. The current drug research & development (R&D) system is long and costly, which does not incentivize finding new drug treatments for neglected diseases.

There are examples of drug treatments that were originally developed to treat cancer which were later "shelved," or not used, when proven to be ineffective for treating cancer. Some years later, researchers will come across this drug treatment and discover that it's actually effective in treating another disease, like a neglected disease.

With the onset of image processing techniques, I wanted to explore the possibility of predicting promising new drug treatments based on their molecular structures.



---

## What's my MVP here?

Given the data provided by Meyer, et. al, I want to explore classifying molecules based on:

1. Chemical molecular structure (provided as images). Ex:
![Chem structure](./test_data/cns/753.png)
2. Chemical SMILES (provided as a string of text). Ex:

  __CCCCCCC(C)(C)c1ccc(C2CC(O)CCC2CCCO)c(O)c1__

I want to compare which model is more accurate at predicting the drug therapy class. If molecular structures perform better, then that implies there is information about the geometric structure of chemicals that is more representative of its properties.

---
## Data

For now, I have copied a subset of the data provided by Meyer, et. al to perform a binary (antineoplastic, or cns) classification model.

The images are split into my train set [here](./train_data) and test set [here](./test_data).

I also want to explore this csv that include more information about the chemical properties:

-[CID_properties.csv](./data/CID_properties.csv):
Includes information  on feature hydrophobe count 3D, H bond acceptor count and H bond donor count.

---

## Modeling

Currently I'm following this [TensorFlow tutorial](https://github.com/tensorflow/docs) for my binary classification. I will expand on this for multiclass classification.
