
import streamlit as st

st.set_page_config(
    page_title="Sparky Sanskrit",
    page_icon="📚",
    layout="centered"
)

if "completed_lessons" not in st.session_state:
    st.session_state.completed_lessons = []

st.title("📚 Sparky Sanskrit")
st.subheader("Learn Sanskrit from Zero to Hero")

st.write(
    "Discover Sanskrit through structured lessons, "
    "quizzes, and the wisdom of Indian knowledge."
)

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Learn Sanskrit", "My Progress", "About"]
)

lessons = {
    "Lesson 1: Greetings": {
        "word": "नमस्ते",
        "meaning": "Greetings / Hello",
        "example": "नमस्ते।",
        "translation": "Greetings."
    },
    "Lesson 2: Thank You": {
        "word": "धन्यवादः",
        "meaning": "Thank you",
        "example": "धन्यवादः।",
        "translation": "Thank you."
    },
    "Lesson 3: Knowledge": {
        "word": "विद्या",
        "meaning": "Knowledge / learning",
        "example": "विद्या ददाति विनयम्।",
        "translation": "Knowledge gives humility."
    }
}

if page == "Home":
    st.header("Welcome, Sanskrit learner! 🙏")
    st.write("Start your journey with your first Sanskrit lesson.")

    if st.button("Start Learning", type="primary"):
        st.session_state.open_lessons = True

    st.info(
        "Learn vocabulary, understand meanings, "
        "and test your knowledge."
    )

    st.subheader("Your learning path")
    st.write("1. Learn basic Sanskrit words")
    st.write("2. Understand simple sentences")
    st.write("3. Practise with quizzes")
    st.write("4. Progress towards reading Sanskrit")

elif page == "Learn Sanskrit":
    st.header("Sanskrit Lessons")

    lesson_name = st.selectbox(
        "Choose a lesson",
        list(lessons.keys())
    )

    lesson = lessons[lesson_name]

    st.markdown(f"## {lesson['word']}")
    st.write("**Meaning:**", lesson["meaning"])
    st.write("**Example:**", lesson["example"])
    st.write("**Translation:**", lesson["translation"])

    if lesson_name in st.session_state.completed_lessons:
        st.success("You have completed this lesson.")
    elif st.button("Mark Lesson Complete"):
        st.session_state.completed_lessons.append(lesson_name)
        st.rerun()

    st.divider()
    st.subheader("Quick Quiz")

    answer = st.radio(
        f"What does {lesson['word']} mean?",
        ["Choose an answer", "Knowledge", "Greetings / Hello", "Thank you"],
        key=lesson_name
    )

    if st.button("Check Answer"):
        correct_answers = {
            "Lesson 1: Greetings": "Greetings / Hello",
            "Lesson 2: Thank You": "Thank you",
            "Lesson 3: Knowledge": "Knowledge"
        }

        if answer == correct_answers[lesson_name]:
            st.success("Correct! Well done.")
        else:
            st.error("Not quite. Review the lesson and try again.")

elif page == "My Progress":
    st.header("My Learning Progress")

    completed = len(st.session_state.completed_lessons)
    total = len(lessons)

    st.metric("Lessons completed", f"{completed} / {total}")
    st.progress(completed / total)

    if completed == total:
        st.success("Excellent! You completed all sample lessons.")
    else:
        st.write("Keep learning and complete your next lesson.")

elif page == "About":
    st.header("About Sparky Sanskrit")
    st.write(
        "Sparky Sanskrit is a learning platform concept "
        "designed to make Sanskrit accessible through "
        "structured lessons and interactive practice."
    )
    st.write(
        "Future versions can add an AI Acharya, "
        "verified Sanskrit sources, user accounts, "
        "and saved learning progress."
    )

st.divider()
st.caption("Sparky Sanskrit | Learning begins with one word.")
