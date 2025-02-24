from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

input_data = [
    [9],
    [10],
    [11],
    [12],
    [13],
    [14],
    [15],
    [16],
]

output_data = [0,10,20,30,40,30,20,10]

model = make_pipeline(PolynomialFeatures(2), Ridge())
model.fit(input_data, output_data)

print(model.predict([[11.5]]))