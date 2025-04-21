import numpy as np
import tensorflow as tf
import matplotlib.image as mpimg
import streamlit as st
from PIL import Image
import pandas as pd

# load model 
model = tf.keras.models.load_model("model.h5")

# labels for the six classes of fruit
classes = ['apple', 'avocado', 'banana', 'kiwi', 'lemon', 'orange']

# format the image to the expected input shape
def format_image(img_path):
    try:
        img = mpimg.imread(img_path)
        resized_image = tf.image.resize(img, (128, 128))
        return resized_image
    except Exception as e:
        st.warning("Please upload a valid image.")
        return None

# generate actual predictions
def get_prediction(resized_image):
    y_pred = model.predict(np.expand_dims(resized_image, 0))
    pred_class = np.argmax(y_pred[0])
    class_name = classes[pred_class]
    return class_name.title()

def main():
    st.title("Fruit Identifier")
    st.subheader('Upload your own fruit image to have it identified')
    
    # list of fruits
    st.write("This is a list of fruits in the training data:")
    
    formatted = pd.DataFrame(classes)
    formatted.columns = ["Fruit"]
    st.dataframe(formatted, width=300, hide_index=True)

    # file uploader for image
    uploaded_file = st.file_uploader("Please select an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.")
    
        # preprocess image
        input_data = format_image(uploaded_file)
    
        # add detect button
        if st.button("Predict Fruit"):
            # display spinner
            with st.spinner("Identifying Fruit..."):
                # make prediction
                predictions = get_prediction(input_data)
    
                # check if prediction is not None
                if predictions is not None:
                    # Display the predictions
                    st.write("### Results:")
                    st.write(predictions)
                else:
                    st.write("Unable to arrive at a prediction")

if __name__ == "__main__":
    main()
