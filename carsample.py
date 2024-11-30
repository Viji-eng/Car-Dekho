import pickle
import pandas as pd
import streamlit as st

# Page configuration
st.set_page_config(page_title="Cardheko Price Prediction", page_icon="🚗", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        color: #f1f1f1;
        background-color: #1E2A47;
        font-family: 'Arial', sans-serif;
    }
    .css-18e3th9 {
        background-color: #1E2A47;
    }
    h1 {
        color: #FF5733 !important;
        text-align: center;
        font-size: 3rem;
        padding: 20px 0;
    }
    h2, h3 {
        color: #f1f1f1 !important;
        font-size: 1.25rem;
    }
    .stSelectbox, .stSlider, .stNumberInput, .stButton {
        background-color: #4B6D8C;  /* Lighter shade of blue */
        color: #FFFFFF;             /* White text for contrast */
        border-radius: 10px;        /* Slightly more rounded corners */
        padding: 12px;              /* Slightly more padding */
        font-size: 1.1rem;          /* Slightly larger text for better readability */

    }
    .stSelectbox, .stSlider {
        margin-bottom: 1rem;
    }
    .stButton {
       .stButton {
    background-color: #4CAF50;  /* Green background */
    color: #ffffff;              /* White text for contrast */
    border-radius: 8px;          /* Rounded corners */
    font-weight: bold;           /* Bold text */
    padding: 12px;               /* Padding inside the button */
    font-size: 1.1rem;           /* Font size for better readability */
}

.stButton:hover {
    background-color: #45a049;  /* Slightly darker green when hovered */
}


    }
    .stButton:hover {
        background-color: #FF4500;
    }
    .stSidebar {
        background-color: #1E2A47;
        color: #f1f1f1;
    }
    .stSidebar .sidebar-content {
        padding-top: 20px;
    }
    .stMarkdown {
        color: #f1f1f1;
    }
    .stNumberInput input {
        background-color: #2E3A59;
    }
    .stSelectbox, .stSlider {
        border: 1px solid #FF5733;
    }

    /* Enhance car details card style */
    .car-details-card {
        background-color: #2E3A59;
        color: #f1f1f1;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        margin: 5px 0;
        max-width: 100%;
        max-height: 400px;
        overflow-y: auto;
    }

    .car-details-card h4 {
        color: #FF5733;
        font-size: 1.2rem;
        font-weight: bold;
    }

    .car-details-card ul {
        list-style-type: none;
        padding: 0;
    }

    .car-details-card ul li {
        margin: 8px 0;
        font-size: 1rem;
    }

    .predicted-price {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF5733;
        text-align: center;
        padding: 20px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Header section
st.markdown("<h1>🚗 Cardheko Price Analysis </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Accurate car resale value estimator!</h3>", unsafe_allow_html=True)
st.write("---")

# Sidebar for car selection input
st.sidebar.header("🚘 Select Car Specifications")

# Load data (Ensure the CSV file path is correct)
Df = pd.read_csv(r"C:/Users/Admin/Downloads/finalmodel.csv")

# Sidebar inputs
Ft = st.sidebar.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Lpg', 'Cng', 'Electric'], index=0)
Bt = st.sidebar.selectbox("Body Type", ['Hatchback', 'SUV', 'Sedan', 'MUV', 'Coupe', 'Minivans', 'Convertibles', 'Hybrids', 'Wagon', 'Pickup Trucks'], index=0)
Tr = st.sidebar.selectbox("Transmission", ['Manual', 'Automatic'], index=1)
Owner = st.sidebar.selectbox("Owner Count", [0, 1, 2, 3, 4, 5], index=0)
Brand = st.sidebar.selectbox("Brand", options=Df['Brand'].unique(), index=0)

# Filter models based on selected Brand, Body Type, and Fuel Type
filtered_models = Df[(Df['Brand'] == Brand) & (Df['body type'] == Bt) & (Df['Fuel type'] == Ft)]['model'].unique()
Model = st.sidebar.selectbox("Model", options=filtered_models)

Model_year = st.sidebar.selectbox("Model Year", options=sorted(Df['modelYear'].unique()), index=0)
IV = st.sidebar.selectbox("Insurance Validity", ['Third Party insurance', 'Comprehensive', 'Zero Dep', 'Not Available'], index=0)
Km = st.sidebar.slider("Kilometers Driven", min_value=100, max_value=100000, step=1000, value=10000)
ML = st.sidebar.number_input("Mileage (kmpl)", min_value=5, max_value=50, step=1, value=15)
Seats = st.sidebar.selectbox("Seats", options=sorted(Df['Seats'].unique()), index=0)
Color = st.sidebar.selectbox("Color", Df['Color'].unique(), index=0)
City = st.sidebar.selectbox("City", options=Df['City'].unique(), index=0)

# Main layout for displaying selected data and predictions
col1, col2 = st.columns([1, 2])

# Display the selected car details in a card style
with col1:
    st.subheader("📝 Selected Car Details")
    st.markdown(
        f"""
        <div class="car-details-card">
            <h4>Fuel Type</h4>
            <p>{Ft}</p>
            <h4>Body Type</h4>
            <p>{Bt}</p>
            <h4>Transmission</h4>
            <p>{Tr}</p>
            <h4>Owner Count</h4>
            <p>{Owner}</p>
            <h4>Brand</h4>
            <p>{Brand}</p>
            <h4>Model</h4>
            <p>{Model}</p>
            <h4>Model Year</h4>
            <p>{Model_year}</p>
            <h4>Insurance Validity</h4>
            <p>{IV}</p>
            <h4>Kilometers Driven</h4>
            <p>{Km}</p>
            <h4>Mileage</h4>
            <p>{ML} kmpl</p>
            <h4>Seats</h4>
            <p>{Seats}</p>
            <h4>Color</h4>
            <p>{Color}</p>
            <h4>City</h4>
            <p>{City}</p>
        </div>
        """, unsafe_allow_html=True
    )

# Prediction section
with col2:
    st.subheader("💡 Price Prediction")
    st.markdown("Click below to predict the resale value of the car:")

    if st.button("Predict Car Price"):
        # Load the model pipeline
        with open(r"C:/Users/Admin/Downloads/pipeline (1).pkl", 'rb') as f:
            pipeline = pickle.load(f)

        # Prepare the input data for the model
        input_data = pd.DataFrame({
            'Fuel type': [Ft],
            'body type': [Bt],
            'transmission': [Tr],
            'ownerNo': [Owner],
            'Brand': [Brand],
            'model': [Model],
            'modelYear': [Model_year],
            'Insurance Validity': [IV],
            'Kms Driven': [Km],
            'Mileage': [ML],
            'Seats': [Seats],
            'Color': [Color],
            'City': [City]
        })

        # Check if all inputs are valid (e.g., non-zero mileage, valid model)
        if Model and Km > 0 and ML > 0:
            # Predict the price using the pipeline
            prediction = pipeline.predict(input_data)
            st.markdown(f"<p class='predicted-price'>🏷️ Estimated Resale Value: ₹ {round(prediction[0], 2)} lakhs</p>", unsafe_allow_html=True)
        else:
            st.error("Please ensure all fields are correctly filled before predicting.")
