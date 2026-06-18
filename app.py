import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Tour Enquiry Dashboard")

df = pd.read_csv("tour_enquiries.csv")

st.subheader("Dataset")
st.dataframe(df)

# Bar Chart
st.subheader("Popular Destinations")

destinations = df.groupby("Destination")["Enquiries"].sum().reset_index()

fig1 = px.bar(
    destinations,
    x="Destination",
    y="Enquiries",
    title="Destination-wise Enquiries"
)

st.plotly_chart(fig1)

# Line Chart
st.subheader("Monthly Trend")

monthly = df.groupby("Month")["Enquiries"].sum().reset_index()

fig2 = px.line(
    monthly,
    x="Month",
    y="Enquiries",
    markers=True,
    title="Monthly Enquiries"
)

st.plotly_chart(fig2)

# Pie Chart
st.subheader("State Distribution")

state_data = df.groupby("State")["Enquiries"].sum().reset_index()

fig3 = px.pie(
    state_data,
    names="State",
    values="Enquiries",
    title="State-wise Enquiries"
)

st.plotly_chart(fig3)