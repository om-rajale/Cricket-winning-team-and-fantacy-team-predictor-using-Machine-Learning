import streamlit as st
import pickle
import pandas as pd

# Load models
pipe = pickle.load(open('new_pipe.pkl', 'rb'))
fantasy_model = pickle.load(open('fantasy_model.pkl', 'rb'))

# Load fantasy data
fantasy_df = pd.read_csv('fantasy_full_cleaned.csv')

# Predefined teams and cities for win predictor
teams_win = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
             'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
             'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

# Extract team and venue options for fantasy predictor
teams_fantasy = sorted(pd.unique(fantasy_df[['home_team_x', 'away_team_x']].values.ravel('K')))
venues = sorted(fantasy_df['venue'].dropna().unique())

# App layout
st.set_page_config(layout="centered")

# Tabs
tab1, tab2 = st.tabs(["🏏 IPL Win Predictor", "⭐ Dream11 Fantasy Team Predictor"])

# --- IPL Win Predictor Tab ---
with tab1:
    st.title('🏏 IPL Win Predictor')

    col1, col2 = st.columns(2)
    with col1:
        batting_team = st.selectbox('Select Batting Team', sorted(teams_win))
    with col2:
        bowling_team = st.selectbox('Select Bowling Team',
                                    sorted([team for team in teams_win if team != batting_team]))

    selected_city = st.selectbox('Select Host City', sorted(cities))

    # Fix NumberInput format/type mismatch
    # Fix NumberInput format/type mismatch using all float types
    target = st.number_input('Target Score', min_value=1.0, step=1.0, format="%.0f", value=1.0)

    col3, col4, col5 = st.columns(3)
    with col3:
        score = st.number_input('Current Score', min_value=0.0, step=1.0, format="%.0f", value=0.0)
    with col4:
        overs = st.number_input('Overs', min_value=0.0, max_value=20.0, step=0.1, format="%.1f", value=0.0)
    with col5:
        wickets = st.number_input('Wickets Out', min_value=0.0, max_value=10.0, step=1.0, format="%.0f", value=0.0)

    if st.button('🔮 Predict Match Win Probability'):
        if overs == 0:
            st.warning("Overs can't be zero!")
        else:
            runs_left = target - score
            balls_left = 120 - int(overs * 6)
            remaining_wickets = 10 - wickets
            crr = score / overs
            rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

            input_df = pd.DataFrame({
                'batting_team': [batting_team],
                'bowling_team': [bowling_team],
                'city': [selected_city],
                'runs_left': [runs_left],
                'balls_left': [balls_left],
                'wickets': [remaining_wickets],
                'total_runs_x': [target],
                'crr': [crr],
                'rrr': [rrr]
            })

            result = pipe.predict_proba(input_df)
            loss = result[0][0]
            win = result[0][1]

            st.success(f"✅ {batting_team} Win Probability: **{round(win * 100)}%**")
            st.error(f"🛑 {bowling_team} Win Probability: **{round(loss * 100)}%**")

# --- Dream11 Fantasy Team Predictor Tab ---
with tab2:
    st.title("⭐ Dream11 Fantasy Team Predictor")

    col1, col2 = st.columns(2)
    with col1:
        team1 = st.selectbox('Select Team 1', teams_fantasy, key='team1')
    with col2:
        team2 = st.selectbox('Select Team 2', [t for t in teams_fantasy if t != team1], key='team2')

    venue = st.selectbox('Select Match Venue', venues)

    if st.button("✨ Predict Fantasy Team"):
        match_players = fantasy_df[
            (((fantasy_df['home_team_x'] == team1) & (fantasy_df['away_team_x'] == team2)) |
             ((fantasy_df['home_team_x'] == team2) & (fantasy_df['away_team_x'] == team1))) &
            (fantasy_df['venue'] == venue)
        ]

        match_players = match_players.sort_values('Predicted_FP', ascending=False)
        match_players = match_players.drop_duplicates(subset='fullName')
        top_players = match_players.head(11).copy()

        st.markdown("### 🏅 Top 11 Predicted Fantasy Players")
        st.dataframe(top_players[['fullName', 'Predicted_FP']].reset_index(drop=True), use_container_width=True)
