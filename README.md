## Monument Valley

Monument Valley is a web application that uses a Convolutional Neural Network (CNN) model for monument detection. The application allows users to upload images of monuments and predicts the type of monument using the trained model.

### Model Architecture

The monument detection model is built using TensorFlow's Keras API. The CNN model architecture consists of multiple convolutional layers, max-pooling layers, and dense layers. Here is the architecture of the model:

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential([
  Conv2D(32, 5, activation='relu', input_shape=(300, 300, 3)),
  MaxPooling2D(),
  Conv2D(32, 5, activation='relu'),
  MaxPooling2D(),
  Conv2D(64, 5, activation='relu'),
  MaxPooling2D(),
  Conv2D(64, 5, activation='relu'),
  MaxPooling2D(),
  Flatten(),
  Dense(512, activation='relu'),
  Dense(128, activation='relu'),
  Dense(64, activation='relu'),
  Dense(17, activation='softmax')
])

model.compile(
  loss="categorical_crossentropy",
  optimizer=tf.keras.optimizers.Adam(),
  metrics=["accuracy"]
)
```

### Model Performance

Monument Valley is a web application that uses a monument detection model with approximately 70% accuracy in both training and test cases. The model has been carefully optimized to avoid underfitting and overfitting issues. It can reliably predict monument types for a wide range of input images, making it a valuable tool for monument enthusiasts and travelers.

### Usage

To use the Monument Valley web application, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run app.py
   ```

4. Upload an image of a monument and explore the predicted monument type, description, location on the map, and related YouTube video.

### Contributions

Contributions to Monument Valley are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

### Dataset

We have used a customized dataset containing 17 classes of different monuments from around the world. We have tried to keep the data as consistent as possible and we have trained the above mentioned model on this dataset.

### License

Monument Valley is released under the [MIT License](LICENSE).

Feel free to modify and enhance this template as per your requirements and project details.
