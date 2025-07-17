import streamlit as st
import pandas as pd
import numpy as np

# -------------------------------
# PART 1: DATA CREATION
# -------------------------------

# Set seed for reproducibility
np.random.seed(42)

players = [
    "Virat Kohli", "Steve Smith", "Kane Williamson", "Jasprit Bumrah",
    "Ravindra Jadeja", "Ben Stokes", "David Warner", "Babar Azam",
    "Rashid Khan", "Hardik Pandya"
]

countries = [
    "India", "Australia", "New Zealand", "India",
    "India", "England", "Australia", "Pakistan",
    "Afghanistan", "India"
]

player_types = [
    "Batsman", "Batsman", "Batsman", "Bowler",
    "All-Rounder", "All-Rounder", "Batsman", "Batsman",
    "Bowler", "All-Rounder"
]

matches = np.random.randint(50, 300, size=10)
runs = np.random.randint(1000, 12000, size=10)
highest_scores = np.random.randint(50, 200, size=10)
wickets = np.random.randint(0, 250, size=10)
economy = np.round(np.random.uniform(3.5, 6.5, size=10), 2)

# Create DataFrame
df = pd.DataFrame({
    "Player Name": players,
    "Country": countries,
    "Player Type": player_types,
    "Matches Played": matches,
    "Runs Scored": runs,
    "Highest Score": highest_scores,
    "Wickets Taken": wickets,
    "Economy Rate": economy
})

# -------------------------------
# PART 2: STREAMLIT APPLICATION
# -------------------------------

st.title("🏏 Cricket Player Performance Dashboard")
st.markdown("""
Welcome to the **Cricket Player Performance Dashboard**!  
Explore stats of top international players — analyze 🧠, visualize 📊, and experiment 💡!
""")

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Filter Players")

selected_types = st.sidebar.multiselect(
    "Select Player Type", options=df["Player Type"].unique(), default=df["Player Type"].unique()
)

selected_countries = st.sidebar.multiselect(
    "Select Country", options=df["Country"].unique(), default=df["Country"].unique()
)

matches_played = st.sidebar.slider(
    "Minimum Matches Played", int(df["Matches Played"].min()), int(df["Matches Played"].max()), 50
)

# Apply filters
filtered_df = df[
    (df["Player Type"].isin(selected_types)) &
    (df["Country"].isin(selected_countries)) &
    (df["Matches Played"] >= matches_played)
]

# --- DISPLAY RAW DATA ---
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)

# --- SUMMARY METRICS ---
st.subheader("📈 Summary Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Runs Scored", int(filtered_df["Runs Scored"].sum()))

with col2:
    st.metric("Total Wickets Taken", int(filtered_df["Wickets Taken"].sum()))

with col3:
    st.metric("Total Matches Played", int(filtered_df["Matches Played"].sum()))

# --- CHARTS ---
st.header("📊 Performance Charts")

st.subheader("Runs Scored by Players")
st.bar_chart(data=filtered_df.set_index("Player Name")["Runs Scored"])

st.subheader("Wickets Taken by Players")
st.area_chart(data=filtered_df.set_index("Player Name")["Wickets Taken"])

# --- DETAILED PLAYER PROFILE ---
st.header("🧍 Detailed Player Profile")

player_list = filtered_df["Player Name"].tolist()
selected_player = st.selectbox("Select a Player", player_list)

player_data = filtered_df[filtered_df["Player Name"] == selected_player].iloc[0]

left, right = st.columns(2)

with left:
    st.image(f"https://placehold.co/200x250?text={selected_player.replace(' ', '+')}", caption=selected_player)

with right:
    st.markdown(f"**Country:** {player_data['Country']}")
    st.markdown(f"**Type:** {player_data['Player Type']}")
    st.markdown(f"**Matches Played:** {player_data['Matches Played']}")
    st.markdown(f"**Runs Scored:** {player_data['Runs Scored']}")
    st.markdown(f"**Highest Score:** {player_data['Highest Score']}")
    st.markdown(f"**Wickets Taken:** {player_data['Wickets Taken']}")
    st.markdown(f"**Economy Rate:** {player_data['Economy Rate']}")

# Career Trend (Fake Yearly Runs)
years = np.arange(2015, 2024)
runs_trend = np.random.randint(200, 1500, size=len(years))
trend_df = pd.DataFrame({"Year": years, "Runs": runs_trend}).set_index("Year")

st.subheader("📉 Career Run Trend")
st.line_chart(trend_df)

# --- INTERACTIVE FORM ---
st.header("🧮 What-if Scenario")

with st.form("hypothetical_form"):
    hypothetical_runs = st.number_input("Add hypothetical runs to this player's total:", min_value=0, max_value=5000, step=100)
    submitted = st.form_submit_button("Calculate")

    if submitted:
        new_total = player_data["Runs Scored"] + hypothetical_runs
        st.success(f"If {selected_player} scores {hypothetical_runs} more runs, their total will be {new_total}!")
        st.balloons()

# --- VIEW SOURCE CODE ---
with st.expander("🧾 View Source Code"):
    st.code("""
# Data creation snippet
players = ["Virat Kohli", "Steve Smith", "Kane Williamson", "Jasprit Bumrah", ...]
matches = np.random.randint(50, 300, size=10)
runs = np.random.randint(1000, 12000, size=10)
...
df = pd.DataFrame({
    "Player Name": players,
    "Country": countries,
    ...
})
    """, language='python')

# -------------------------------
# PART 3: EXPLANATION
# -------------------------------

st.markdown("---")
st.header("🧠 Explanation of Streamlit Functions Used")
