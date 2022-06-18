---
tags:
  - WIP
---

# TNMFML

<small><p style="text-align:right;margin-top:-76px">16/01/2022</p></small>

a.k.a. _Taking Notes on [Making Friends with Machine Learning](https://www.youtube.com/playlist?list=PLRKtJ4IpxJpDxl0NTvNYQWKCYzHNuy2xG)_: notes on applications, processes and big ideas underlying ML.

!!! info "Disclaimer"
    I really enjoyed watching the entire playlist MFML by [Cassie Kozyrkov](https://twitter.com/quaesita), so I decided to watch it a second time while taking notes. Therefore, below you can find those notes, meaning essentially that: all credits for crystal clear explanations, brilliant examples and fun ideas go to Cassie, while biases and misunderstandings are all on me.

!!! warning "Warning"
    This section is a work in progress.

## Introduction

Machine Learning (ML) can be defined as

> an approach to (repeatedly and algorithmically) make lots of small decisions using data finding patterns and recipes that deal correctly with brand new data.

We can think to ML as a _thing labeller_: it gets input data and "learns" recipes from it to produce output labels, in contrast to traditional programming where recipes are basically handcrafted.

The task is to learn how to **succeed on new data**: we are looking for _generalization_ capabilities, not only memorization ones (for which good old lookup tables are all you need).

In doing so, ML methods can find patterns even if they actually aren't there (just like our human brains): that's why you need to test recipes on new data, no matter where they come from.

!!! important "Recipe"
    A _recipe_ is a set of instructions to turn inputs into outputs.

### The kitchen analogy

| Kitchen     | Machine Learning |
| ----------- | ---------------- |
| Ingredients | Data             |
| Appliances  | Algorithms       |
| Recipes     | Models           |
| Dishes      | Predictions      |
| Cook        | Developer        |

Doing ML is just like trying to cook a brand new dish: you don't know the exact procedure to turn all your ingredients in the tasty dish beforehand, but you proceed by trials and fails, gaining more and more experience on the way.

## 12 Steps of ML

| Steps     | Topic                                                    | Notes                                                       |
| ----------| -------------------------------------------------------- | ----------------------------------------------------------- |
| 0 - 1     | Ask the right questions                                  | What's the task? Which is the benchmark? What's a success?  |
| 2 - 3 - 4 | Get the right data                                       | Get ingredients! At scale, you will need _data engineering_ |
| 5 - 6 - 7 | Use algorithms to make recipes from patterns in the data | Iterating towards better recipes                            |
| 8 - 9     | Check recipes on new data                                | Validate and then test                                      |
| 10        | Build a production-ready system                          | From prototype to production (requires investments!)        |
| 11        | Make sure you want to launch                             | Cautiously test on few customers                            |
| 12        | Ensure reliability over time                             | Monitor and maintain                                        |

Several roles/skills are involved in an ML projects <small>not all necessarily assumed by different individuals</small>:

- Decision maker
- Domain expert
- Statistician
- Engineer
- Analyst

### S00 - Find a task

### S01 - Set objective

### S02 - Get data

### S03 - Split data

### S04 - Explore data

### S05 - Get tools

### S06 - Model: train

### S07 - Model: tune and debug

### S08 - Model: validate

### S09 - Model: test

### S10 - Go prod

### S11 - Launch

### S12 - Monitor and maintain

## Inside the Black Box

### k-means

### k-NN

### SVM

### Tree-based methods

### Naive Bayes

### Linear Regression

### Logistic Regression

### Neural Networks
