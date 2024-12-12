import streamlit as st
from PIL import Image
import torch
from torchvision import transforms

# Load the pretrained model
model = torch.load('model.pkl')
model.eval()

# Define image transformation
transform = transforms.Compose([
    transform.Resize((640, 640)),
    transforms.ToTensor(),
])

# Streamlit app
st.title("This app can detect if there is any field island on an image")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "tif"])

if uploaded_file is not None:
    # Open the image file
    image = Image.open(uploaded_file)
    
    # Display the image
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Transform the image
    image = transform(image).unsqueeze(0)
    
    # Classify the image
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
        class_name = 'Present' if predicted.item() == 1 else 'Absent'
    
    # Display the classification result
    st.write(f"Field island is {class_name}")