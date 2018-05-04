# Regression Connectome
Experiments regarding the creation of graphs describing bidirectional relations between feature nodes for homogeneous prediction

## Background
Machine learning is all about making inferences and predictions on new data. The training features are usually isolated from the output results. 

In a supervised learning scenario, creating a model which would predict Y by using X requires the collection of data points which contain both input and output data. Those data points are used to create a directed relation between X and Y. In order to reverse the problem, the model has to be restructured and retrained, having only one purpose at a time. Additionally, the model is blind to valuable insights regarding correlations between elements from X alone and elements from Y alone. Classical machine learning models discriminate data by treating data features differently at a high level. It narrows the model to a specific problem, despite the possibilities of a homogenous data connectome.

### Example
The [Iris Dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) data set consists of 50 samples from each of three species of Iris. Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. 

A classical approach is to specificy a task, e.g. predict the petal width from the other features. A machine learning model, like a multilayer perceptron would be trained on the (X -> Y) pairs. Alternatively, information describing the internal area from the petal width would not be harnessed (Y -> X). Neither would the information describing the sepal width from the sepal length (X -> X).

### Process
At first, a complete graph is created with a node for each feature (4 in our case). Then, a linear regression is trained between every two nodes (for a total of 12 in our Iris case).
![Graph](https://github.com/paubric/python-regression-connectome/blob/master/graph.png)
After training we have obtained the following values for slopes and intercepts.
```
(0, 1) [-0.05726823] [0.42088597]
(0, 2) [1.85750967] [-0.89867058]
(0, 3) [0.75384088] [-0.41421703]
(1, 0) [-0.20887029] [0.81542772]
(1, 2) [-1.71120139] [1.11712251]
(1, 3) [-0.62754618] [0.3785177]
(2, 0) [0.4091259] [0.54442026]
(2, 1) [-0.10333897] [0.42719011]
(2, 3) [0.41641913] [-0.05447079]
(3, 0) [0.88751905] [0.61131356]
(3, 1) [-0.20257264] [0.40725126]
(3, 2) [2.22588531] [0.15553342]
```
In this experiment we compare the cost of the **average** of the 3 regression results toward one node to the individual results. The average regression performance is, effectively, above average, being the best in half the cases.
```
Cost:  0.0
Cost:  1.7749370367472766e-28
Cost:  1.0366125332669858e-29
Cost:  3.520415049065206e-28
Special cost:  1.601880675664417e-28 

Cost:  1.1093356479670479e-29
Cost:  0.0
Cost:  4.930380657631324e-30
Cost:  4.686943112660777e-30
Special cost:  6.039716305598372e-31 

Cost:  7.888609052210118e-29
Cost:  2.0194839173657902e-28
Cost:  0.0
Cost:  1.2823920090499073e-28
Special cost:  1.262177448353619e-29 

Cost:  7.888609052210118e-29
Cost:  2.8398992587956425e-29
Cost:  2.2790684589900794e-29
Cost:  0.0
Special cost:  3.865418435582958e-29 
```
