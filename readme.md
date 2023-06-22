## Mushroom Edibility Prediction

This project aims to predict the edibility of mushrooms based on a dataset containing 20 features. It utilizes two machine learning models, namely Feature Standardizer and Ridge Regression, to make accurate predictions. The models have been trained on a labeled mushroom dataset.

### Features Used
The following features have been used to train the models:

- cap_shape
- cap_surface
- cap_color
- bruises
- odor
- gill_attachment
- gill_spacing
- gill_size
- gill_color
- stalk_shape
- stalk_root
- stalk_surface_above_ring
- stalk_surface_below_ring
- stalk_color_above_ring
- stalk_color_below_ring
- ring_number
- ring_type
- spore_print_color
- population
- habitat

### Output
The output of the prediction is represented as a binary value, where 0 indicates the mushroom is not edible, and 1 indicates it is edible.

### Installation and Setup
To run this project locally, follow these steps:

1. Clone the repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Install the required libraries by running the following command:
   ```
   pip install pandas numpy scikit-learn
   ```
4. Run the project by executing the Python script.

### Models Used

The models used in this project are as follows:

1. Feature Standardizer:
   - This model standardizes the input features before passing them to the Ridge Regression model.
   - Standardization ensures that the features are scaled appropriately, improving the performance of the Ridge Regression model.

2. Ridge Regression:
   - This model predicts the edibility of mushrooms based on the standardized features.
   - It has been trained on a labeled mushroom dataset and achieves an accuracy of approximately 73%.

### Further Improvements

While the current implementation provides a functional solution for predicting mushroom edibility, there are several areas where improvements can be made:

- Increasing the dataset size: Collecting a larger and more diverse dataset of mushrooms can help improve the accuracy of the models.
- Exploring different machine learning algorithms: Trying out different algorithms and comparing their performance could lead to better results.
- Fine-tuning hyperparameters: Tuning the hyperparameters of the models could potentially improve the accuracy further.

Feel free to contribute to this project or make any necessary improvements to better suit your needs.