import numpy as np
 
np.random.seed(1)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])
 
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
 
W1 = np.random.randn(2, 4)
b1 = np.zeros((1, 4))
W2 = np.random.randn(4, 1)
b2 = np.zeros((1, 1))
lr = 1.0
 
for epoch in range(10001):
    hidden = sigmoid(X @ W1 + b1)
    output = sigmoid(hidden @ W2 + b2)
    error = y - output
    d_out = error * output * (1 - output)
    d_hid = (d_out @ W2.T) * hidden * (1 - hidden)
    W2 += hidden.T @ d_out * lr
    b2 += d_out.sum(axis=0, keepdims=True) * lr
    W1 += X.T @ d_hid * lr
    b1 += d_hid.sum(axis=0, keepdims=True) * lr
    if epoch % 2000 == 0:
        print("Epoch %5d  loss = %.5f" % (epoch, np.mean(error ** 2)))
 
print("\nInput -> Output (rounded)")
for xi, oi in zip(X, output):
    print(xi, "->", round(float(oi[0]), 3), "=>", int(oi[0] > 0.5))
