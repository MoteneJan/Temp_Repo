import streamlit as st
import numpy as np
from PIL import Image

# Setting the page configuration
st.set_page_config(page_title="Height Segmentation Model", layout="wide")

# Sidebar for navigation
st.sidebar.title("Height Segmentation App")
st.sidebar.markdown('<style>div.row {display: flex;}</style>', unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='color: white;'>Navigation Pages</h3>", unsafe_allow_html=True)

# Sidebar options
page = st.sidebar.selectbox("Select Page", ["Home", "Predictions", "Insights", "Others"])

# Home Page
if page == "Home":
    st.title("Welcome to Height Segmentation Model")
    st.markdown("""
    This application allows users to upload satellite images and receive height and segmentation predictions based on a trained model.
    """)

    # Display two images horizontally
    # col1, col2 = st.columns(2)
    
    # with col1:
    st.image("sample.png")  

    # with col2:
    #     st.image("mask.png", caption='Segmented Image')  

# Predictions Page
elif page == "Predictions":
    st.title("Make Predictions")
    
    # Model selection
    model_type = st.selectbox("Select Model Type", ["Height Model", "Segmentation Model"])

    # Sample images for testing
    st.subheader("Select Samples from Test Set")
    
    sample_images = {
        "Sample Image 1": "test_image1.jpg", 
        "Sample Image 2": "test_image2.jpg",
        "Sample Image 3": "test_image3.jpg"
    }
    
    selected_image = None
    
    # Create columns for sample images and buttons
    cols = st.columns(len(sample_images))
    
    for i, (name, path) in enumerate(sample_images.items()):
        if cols[i].button(name):
            selected_image = Image.open(path)
            cols[i].image(selected_image, caption=f'Selected {name}', use_column_width=True)

    # Upload image section
    uploaded_file = st.file_uploader("Or Upload Your Own Satellite Image", type=["jpg", "png"])
    uploaded_mask_file = st.file_uploader("Upload Corresponding Mask Data", type=['png', 'jpg', 'jpeg'])

    if uploaded_file and uploaded_mask_file is not None:
        selected_image = Image.open(uploaded_file)
        mask_image = Image.open(uploaded_mask_file)

        # Display the uploaded satellite image and its corresponding mask
        col1, col2 = st.columns(2)
        with col1:
            st.image(selected_image, caption='Uploaded Satellite Image', use_column_width=True)
        
        with col2:
            st.image(mask_image, caption='Corresponding Mask', use_column_width=True)
        
        st.write("Mask data uploaded successfully.")

    if selected_image is not None:
        # Model prediction section
        if st.button("Run Model"):
            # Here we call model's prediction function based on selected model_type
            # For demonstration, we will create a dummy output while we are working on models 
            segmentation_output = np.random.rand(*selected_image.size[::-1], 3)  # Dummy segmentation output

            # Display segmentation result based on selected model type
            if model_type == "Height Model":
                st.image(segmentation_output, caption='Height Output')
                st.subheader("Performance Metrics for Height Model")
                st.write("Mean Absolute Error: 0.5")  

            elif model_type == "Segmentation Model":
                st.image(segmentation_output, caption='Segmentation Output')
                st.subheader("Performance Metrics for Segmentation Model")
                st.write("Dice Score: 0.85")  

# Insights Page
elif page == "Insights":
    st.title("Insights")
    st.markdown("""
    Here you can find insights related to the model's performance and its impact on radio frequency propagation.
    - **Understanding Clutter**: Clutter data is essential for optimizing network design.
    - **Model Performance**: Regular evaluations are crucial for maintaining accuracy in predictions.
    """)

# Footer section
st.markdown("""
### About This App
This application aims to assist in optimizing telecommunications network design by providing accurate height and segmentation outputs from satellite imagery.
""")