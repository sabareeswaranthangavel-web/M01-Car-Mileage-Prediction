# M01 – Car Mileage Prediction Using Linear Regression

## Project Overview
This project predicts the mileage of a car based on its weight using Machine Learning. Linear Regression is used to identify the relationship between vehicle weight and fuel efficiency.

## Objective
To develop a Machine Learning model that predicts car mileage (MPG) using car weight as the input feature.

## Dataset
- **Dataset:** Auto MPG Dataset
- **Source:** [Kaggle – Auto MPG Dataset](https://www.kaggle.com/datasets/uciml/autompg-dataset)
- **Total Records:** 398 cars
- **Input:** Car Weight (pounds)
- **Output:** Mileage (miles per gallon)

## Technologies Used
- Python
- Pandas
- Matplotlib
- Scikit-learn
- Linear Regression

## Methodology
1. Load the Auto MPG dataset.
2. Clean missing values.
3. Select car weight as the input feature and mileage as the target.
4. Split the dataset into 80% training and 20% testing data.
5. Train the Linear Regression model.
6. Evaluate model performance.
7. Predict mileage for a car weighing 3000 pounds.
8. Visualize the results using a regression graph.

## Model Performance

| Evaluation Metric | Result |
|---|---:|
| R² Score | 0.723 |
| Mean Absolute Error | 3.12 MPG |
| Slope | -0.0078 |
| Intercept | 46.78 |

## Prediction Result
**Input:** Car weight = 3000 pounds

**Predicted Output:** 23.37 MPG

## Output
The regression graph illustrates the relationship between car weight and mileage. It shows a negative correlation, indicating that heavier cars generally have lower fuel efficiency.

## Project Structure
```text
M01-Car-Mileage-Prediction/
│
├── auto-mpg.csv
├── m01.py
├── README.md
└── output.png
```

## How to Run
Install the required libraries:

```bash
python -m pip install pandas matplotlib scikit-learn
```

Run the project:

```bash
python m01.py
```

## Conclusion
The Linear Regression model successfully demonstrates the relationship between car weight and fuel efficiency. The model achieved an R² score of 0.723, showing that car weight is a useful factor for predicting mileage.

This project provides a basic understanding of Machine Learning implementation in mechanical engineering applications.
