# Regression Connectome
Experiments regarding the creation of graphs describing bidirectional relations between feature nodes for homogeneous prediction

## Background
Machine learning is all about making inferences and predictions on new data. The training features are usually isolated from the output results. 

In a supervised learning scenario, creating a model which would predict Y by using X requires the collection of data points which contain both input and output data. Those data points are used to create a directed relation between X and Y. In order to reverse the problem, the model has to be restructured and retrained, having only one purpose at a time. Additionally, the model is blind to valuable insights regarding correlations between elements from X alone and elements from Y alone. Classical machine learning models discriminate data by treating data features differently at a high level. It narrows the model to a specific problem, despite the possibilities of a homogenous data connectome.

### Example:
Lets assume a dataset which contains features describing sold houses. It contains the following for each house:
- Price at which it was sold
- Number of rooms
- Internal area
- Year built

A classical approach is to specificy a task, e.g. predict the price from the other features. A machine learning model, like a multilayer perceptron would be trained on the X -> Y pairs. Alternatively, information describing the internal area from the price would not be harnessed Y -> X. Neither would the information describing the internal area from the number of rooms X -> X.
