import streamlit as st
import pandas as pd

# -----------------------------
# 1. Page config
# -----------------------------
st.set_page_config(page_title="Student Success & Wellness Simulator",
                   layout="centered")

st.title("🎓 Student Success & Wellness Simulator")
st.write(
    "This app simulates how daily habits (study, sleep, stress, screen time, "
    "and attendance) affect a student's performance and XP level."
)

# -----------------------------
# 2. Scoring functions
# -----------------------------
def calculate_performance(study, sleep, stress, attendance, screen, breaks):
    """Weighted performance score (same logic as notebook)."""
    score = (
        (study * 0.30) +
        (sleep * 0.25) +
        (attendance * 0.30) -
        (screen * 0.10) -
        (stress * 0.20) +
        (5 if breaks == "yes" else 0)
    )
    return max(0, round(score, 2))

def calculate_xp(study, sleep, stress, attendance, screen, breaks):
    """Gamified XP + level calculation."""
    xp = 0
    xp += study * 10
    xp += sleep * 8
    xp += (attendance / 10) * 5
    xp -= screen * 3
    xp -= stress * 2
    xp += 15 if breaks == "yes" else 5

    level = xp // 100
    return max(0, round(xp, 2)), int(level)

# -----------------------------
# 3. Session state for history
# -----------------------------
if "history" not in st.session_state:
    st.session_state["history"] = pd.DataFrame(
        columns=["Study", "Sleep", "Stress", "Attendance",
                 "Screen", "Breaks", "Performance", "XP", "Level"]
    )

# -----------------------------
# 4. Input widgets (left sidebar)
# -----------------------------
st.sidebar.header("📥 Enter your daily habits")

study = st.sidebar.slider("Study hours", 0.0, 12.0, 4.0, 0.5)
sleep = st.sidebar.slider("Sleep hours", 0.0, 12.0, 7.0, 0.5)
stress = st.sidebar.slider("Stress level (1–10)", 1, 10, 4)
attendance = st.sidebar.slider("Attendance (%)", 0, 100, 75)
screen = st.sidebar.slider("Screen time (hours)", 0.0, 10.0, 3.0, 0.5)
breaks_taken = st.sidebar.radio("Breaks taken?", ["yes", "no"])

run_button = st.sidebar.button("Run Simulation")

# -----------------------------
# 5. Run simulation on click
# -----------------------------
if run_button:
    performance = calculate_performance(
        study, sleep, stress, attendance, screen, breaks_taken
    )
    xp, level = calculate_xp(
        study, sleep, stress, attendance, screen, breaks_taken
    )

    # Add to history
    new_row = {
        "Study": study,
        "Sleep": sleep,
        "Stress": stress,
        "Attendance": attendance,
        "Screen": screen,
        "Breaks": breaks_taken,
        "Performance": performance,
        "XP": xp,
        "Level": level
    }
    st.session_state["history"] = pd.concat(
        [st.session_state["history"], pd.DataFrame([new_row])],
        ignore_index=True
    )

# -----------------------------
# 6. Show current results
# -----------------------------
history = st.session_state["history"]

if history.empty:
    st.info("Run the simulation from the sidebar to see your performance.")
else:
    latest = history.iloc[-1]

    st.subheader("Current Session Results")
    col1, col2, col3 = st.columns(3)
    col1.metric("Performance Score", latest["Performance"])
    col2.metric("XP Earned", latest["XP"])
    col3.metric("Level", latest["Level"])

    # Simple feedback
    st.write("### Feedback")
    if study < 2:
        st.write("- Study more consistently.")
    if sleep < 7:
        st.write("- Aim for at least **7 hours** of sleep.")
    if stress > 7:
        st.write("- Stress is high — try relaxation or breaks.")
    if attendance < 80:
        st.write("- Attendance is low — try to attend more classes.")
    if screen > 4:
        st.write("- Reduce screen time during study hours.")
    if study >= 3 and sleep >= 7 and stress <= 5:
        st.write(" Great routine! You are balancing your habits well.")

    # -------------------------
    # 7. History table & charts
    # -------------------------
    st.subheader(" Session History")
    st.dataframe(history, use_container_width=True)

    st.subheader("Performance Trend")
    st.line_chart(history["Performance"])

    st.subheader("XP Progress Over Sessions")
    st.line_chart(history["XP"])