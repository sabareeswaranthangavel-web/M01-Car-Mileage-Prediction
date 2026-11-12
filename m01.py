# Project M01: Car mileage from car weight
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# STEP 1: Load the data file (it must be in the same folder)
df = pd.read_csv("auto-mpg.csv")
print("Rows and columns:", df.shape)

# STEP 2: Clean the data
df = df.dropna(subset=["weight", "mpg"])

# STEP 3: Choose input X and output y
X = df[["weight"]]          # double brackets: X must be a table
y = df["mpg"]

# STEP 4: Split: 80% to train, 20% to test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# STEP 5: Train the model (find the best straight line)
model = LinearRegression()
model.fit(X_train, y_train)

# STEP 6: Test on the hidden 20%
y_pred = model.predict(X_test)
print("R2 score:", round(r2_score(y_test, y_pred), 3))
print("Average error:", round(mean_absolute_error(y_test, y_pred), 2), "mpg")
print("Slope m:", round(model.coef_[0], 4))
print("Intercept c:", round(model.intercept_, 2))

# STEP 7: Predict a new value and draw the graph
new = pd.DataFrame({"weight": [3000]})
print("Predicted mileage for weight=3000:", round(model.predict(new)[0], 2), "mpg")

line_x = pd.DataFrame({"weight": sorted(X["weight"])})
plt.scatter(X_test["weight"], y_test, alpha=0.6, label="Actual (test data)")
plt.plot(line_x["weight"], model.predict(line_x), color="red", label="Regression line")
plt.xlabel("Car weight (pounds)")
plt.ylabel("Mileage (miles per gallon)")
plt.title("Car mileage from car weight")
plt.legend()
plt.show()