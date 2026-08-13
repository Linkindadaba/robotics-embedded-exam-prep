import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from generate_pdf import QUESTIONS_DATA, build_pdf

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="RCPS 420: Robotics & Embedded Systems Exam Prep",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ensure PDF exists
PDF_FILENAME = "robotics_embedded_exam_guide.pdf"
if not os.path.exists(PDF_FILENAME):
    build_pdf(PDF_FILENAME)

# ---------------------------------------------------------
# Custom CSS for High Contrast & Readability
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Dark Slate Background */
    .stApp {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
    }
    
    /* Main Titles */
    .main-title {
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
        background: linear-gradient(90deg, #38BDF8, #818CF8, #C084FC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    
    .sub-title {
        color: #CBD5E1 !important;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }
    
    /* Question Card Box */
    .q-card {
        background-color: #1E293B !important;
        border: 2px solid #334155 !important;
        border-radius: 12px;
        padding: 20px 24px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        margin-bottom: 20px;
    }
    
    .q-card h3 {
        color: #FFFFFF !important;
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        margin-top: 8px !important;
    }

    /* Streamlit Radio Buttons Text & Labels Fix */
    div[data-testid="stRadio"] label p {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: #FFFFFF !important;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] label {
        background-color: #1E293B !important;
        border: 1px solid #475569 !important;
        border-radius: 8px !important;
        padding: 12px 18px !important;
        margin-bottom: 10px !important;
        transition: all 0.2s ease-in-out;
        cursor: pointer !important;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
        background-color: #334155 !important;
        border-color: #38BDF8 !important;
    }
    
    /* Checked radio button highlight */
    div[data-testid="stRadio"] div[role="radiogroup"] label[aria-checked="true"] {
        background-color: #1E3A8A !important;
        border: 2px solid #38BDF8 !important;
    }

    /* All General Paragraphs & Text */
    p, span, label, div {
        color: #F8FAFC;
    }

    /* Selectbox & Dropdown Label & Options */
    div[data-testid="stSelectbox"] label p {
        color: #38BDF8 !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
    }
    
    div[data-baseweb="select"] {
        background-color: #1E293B !important;
        border-color: #475569 !important;
        color: #FFFFFF !important;
    }

    div[data-baseweb="select"] * {
        color: #FFFFFF !important;
    }

    /* Badges */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    
    .badge-embedded { background: #0284C7; color: #FFFFFF; }
    .badge-sensors { background: #EA580C; color: #FFFFFF; }
    .badge-fundamentals { background: #9333EA; color: #FFFFFF; }
    .badge-kinematics { background: #16A34A; color: #FFFFFF; }

    /* Explanation Box */
    .explanation-box {
        background-color: #0F172A !important;
        border-left: 5px solid #38BDF8 !important;
        border-radius: 8px;
        padding: 16px;
        margin-top: 15px;
        color: #F8FAFC !important;
    }
    
    .explanation-box h4 {
        color: #38BDF8 !important;
        margin-bottom: 8px !important;
    }

    /* Expander Styling */
    .stExpander {
        background-color: #1E293B !important;
        border: 1px solid #475569 !important;
        border-radius: 10px !important;
    }
    
    .stExpander summary p {
        color: #38BDF8 !important;
        font-weight: 700 !important;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0F172A !important;
        border-right: 1px solid #334155 !important;
    }

    section[data-testid="stSidebar"] label p {
        color: #F8FAFC !important;
        font-size: 1rem !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        border: none !important;
        padding: 8px 16px !important;
    }

    .stButton>button:hover {
        background-color: #1D4ED8 !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
    }
    
    /* Footer removal */
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar & Navigation
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/isometric/96/robot.png", width=70)
    st.markdown("### **RCPS 420 Exam Portal**")
    st.caption("Sunyani Technical University | Robotics & Embedded Systems")
    
    st.divider()
    
    mode = st.radio(
        "Navigation",
        ["🎯 Practice Quiz Mode", "⏱️ Full Mock Exam", "📚 Solved Q&A Bank & PDF", "📊 Topic Analytics"],
        index=0
    )
    
    st.divider()
    
    st.markdown("#### 📥 Download Revision PDF")
    with open(PDF_FILENAME, "rb") as f:
        pdf_bytes = f.read()
    st.download_button(
        label="📄 Download Solved Q&A (PDF)",
        data=pdf_bytes,
        file_name="Robotics_Embedded_Systems_Exam_Guide.pdf",
        mime="application/pdf",
        use_container_width=True
    )
    
    st.caption("Designed for student revision & peer study groups.")

# Helper badge renderer
def get_badge_html(cat):
    if "Embedded" in cat:
        return f'<span class="badge badge-embedded">{cat}</span>'
    elif "Sensors" in cat:
        return f'<span class="badge badge-sensors">{cat}</span>'
    elif "Fundamentals" in cat:
        return f'<span class="badge badge-fundamentals">{cat}</span>'
    else:
        return f'<span class="badge badge-kinematics">{cat}</span>'

# ---------------------------------------------------------
# Mode 1: 🎯 Practice Quiz Mode
# ---------------------------------------------------------
if mode == "🎯 Practice Quiz Mode":
    st.markdown('<h1 class="main-title">🎯 Interactive Practice Quiz</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Select an option to test your answer and unlock the step-by-step solution.</p>', unsafe_allow_html=True)
    
    col_cat, col_num = st.columns([2, 1])
    with col_cat:
        categories = ["All Topics", "Embedded Systems", "Sensors & Actuators", "Robotics Fundamentals", "Robotics & Kinematics"]
        selected_cat = st.selectbox("Filter by Category", categories)
    
    filtered_qs = QUESTIONS_DATA if selected_cat == "All Topics" else [q for q in QUESTIONS_DATA if q["category"] == selected_cat]
    
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
        
    if st.session_state.q_index >= len(filtered_qs):
        st.session_state.q_index = 0
        
    with col_num:
        q_options = [f"Question {q['id']}" for q in filtered_qs]
        selected_q_label = st.selectbox("Jump to Question", q_options, index=st.session_state.q_index)
        st.session_state.q_index = q_options.index(selected_q_label)
        
    q = filtered_qs[st.session_state.q_index]
    
    st.progress((st.session_state.q_index + 1) / len(filtered_qs))
    st.caption(f"Question {st.session_state.q_index + 1} of {len(filtered_qs)}")
    
    # Render Question Card
    st.markdown(f'<div class="q-card">{get_badge_html(q["category"])}<h3>Q{q["id"]}. {q["question"]}</h3></div>', unsafe_allow_html=True)
    
    # Require explicit selection before showing answer (index=None)
    user_choice = st.radio(
        "Select your answer below:",
        q["options"],
        index=None,
        key=f"prac_{q['id']}"
    )
    
    # Only reveal answer and explanation AFTER user clicks an option
    if user_choice is not None:
        correct_prefix = q["answer"][:3]
        user_prefix = user_choice[:3]
        
        if user_prefix == correct_prefix:
            st.success(f"🎉 **Correct!** Answer is **{q['answer']}**")
        else:
            st.error(f"❌ **Incorrect.** You selected {user_choice}. Correct answer is **{q['answer']}**")
            
        with st.expander("💡 View Detailed Explanation & Lecture Reference", expanded=True):
            st.markdown(f"""
            <div class="explanation-box">
                <h4><b>Correct Answer:</b> {q['answer']}</h4>
                <p>{q['explanation']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("👆 **Choose one of the options above to reveal the correct answer and explanation.**")
            
    st.divider()
    c1, c2, c3 = st.columns([1, 4, 1])
    with c1:
        if st.button("⬅️ Previous") and st.session_state.q_index > 0:
            st.session_state.q_index -= 1
            st.rerun()
    with c3:
        if st.button("Next ➡️") and st.session_state.q_index < len(filtered_qs) - 1:
            st.session_state.q_index += 1
            st.rerun()

# ---------------------------------------------------------
# Mode 2: ⏱️ Full Mock Exam
# ---------------------------------------------------------
elif mode == "⏱️ Full Mock Exam":
    st.markdown('<h1 class="main-title">⏱️ Full Mock Examination</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Complete all 42 questions under exam conditions with high-contrast choices.</p>', unsafe_allow_html=True)
    
    with st.form("mock_exam_form"):
        user_answers = {}
        for idx, q in enumerate(QUESTIONS_DATA):
            st.markdown(f"### **Q{q['id']}.** {q['question']}")
            user_answers[q['id']] = st.radio(
                f"Options for Q{q['id']}",
                q['options'],
                key=f"mock_{q['id']}",
                index=None
            )
            st.divider()
            
        submitted = st.form_submit_button("🏁 Submit Exam & View Results", type="primary", use_container_width=True)
        
    if submitted:
        score = 0
        total = len(QUESTIONS_DATA)
        category_scores = {}
        
        for q in QUESTIONS_DATA:
            cat = q["category"]
            if cat not in category_scores:
                category_scores[cat] = {"correct": 0, "total": 0}
            category_scores[cat]["total"] += 1
            
            ans = user_answers.get(q['id'])
            if ans and ans[:3] == q['answer'][:3]:
                score += 1
                category_scores[cat]["correct"] += 1
                
        pct = (score / total) * 100
        
        st.balloons()
        st.markdown("## 📊 Exam Performance Scorecard")
        
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Final Score", f"{score} / {total}")
        col_m2.metric("Percentage", f"{pct:.1f}%")
        col_m3.metric("Status", "PASSED 🎉" if pct >= 50 else "NEEDS REVISION ⚠️")
        
        st.subheader("Category Breakdown")
        for cat, data in category_scores.items():
            cat_pct = (data["correct"] / data["total"]) * 100
            st.write(f"**{cat}**: {data['correct']} / {data['total']} ({cat_pct:.1f}%)")
            st.progress(data["correct"] / data["total"])
            
        st.divider()
        st.subheader("Review Incorrect Answers")
        for q in QUESTIONS_DATA:
            ans = user_answers.get(q['id'])
            if not ans or ans[:3] != q['answer'][:3]:
                with st.expander(f"❌ Q{q['id']}. {q['question'][:80]}..."):
                    st.write(f"**Your Answer:** {ans if ans else 'Not Answered'}")
                    st.write(f"**Correct Answer:** {q['answer']}")
                    st.info(f"**Explanation:** {q['explanation']}")

# ---------------------------------------------------------
# Mode 3: 📚 Solved Q&A Bank & PDF
# ---------------------------------------------------------
elif mode == "📚 Solved Q&A Bank & PDF":
    st.markdown('<h1 class="main-title">📚 Solved Question Bank</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Search, filter, and review all 42 exam questions with full explanations.</p>', unsafe_allow_html=True)
    
    search_term = st.text_input("🔍 Search questions or keywords...", "")
    
    display_qs = QUESTIONS_DATA
    if search_term:
        display_qs = [q for q in QUESTIONS_DATA if search_term.lower() in q['question'].lower() or search_term.lower() in q['explanation'].lower()]
        
    st.write(f"Showing **{len(display_qs)}** of 42 questions")
    
    for q in display_qs:
        with st.expander(f"Q{q['id']}. {q['question']}"):
            st.markdown(f"**Category:** {get_badge_html(q['category'])}", unsafe_allow_html=True)
            for opt in q['options']:
                if opt[:3] == q['answer'][:3]:
                    st.markdown(f"✅ <span style='color: #4ADE80; font-weight: bold;'>{opt} (Correct Answer)</span>", unsafe_allow_html=True)
                else:
                    st.markdown(f"• <span style='color: #F8FAFC;'>{opt}</span>", unsafe_allow_html=True)
            st.info(f"**Explanation:** {q['explanation']}")

# ---------------------------------------------------------
# Mode 4: 📊 Topic Analytics
# ---------------------------------------------------------
elif mode == "📊 Topic Analytics":
    st.markdown('<h1 class="main-title">📊 Course Topic Distribution</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Statistical breakdown of topics tested in the RCPS 420 Robotics & Embedded Systems Exam.</p>', unsafe_allow_html=True)
    
    df = pd.DataFrame(QUESTIONS_DATA)
    counts = df['category'].value_counts()
    
    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor('#0F172A')
    ax.set_facecolor('#1E293B')
    
    colors = ['#38BDF8', '#FB923C', '#C084FC', '#4ADE80']
    bars = ax.barh(counts.index, counts.values, color=colors[:len(counts)])
    
    ax.set_xlabel('Number of Questions', color='#F8FAFC')
    ax.set_title('Question Count per Subject Category', color='#F8FAFC', fontsize=14, fontweight='bold')
    ax.tick_params(colors='#F8FAFC')
    for spine in ax.spines.values():
        spine.set_color('#475569')
        
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.2, bar.get_y() + bar.get_height()/2, f'{int(width)}',
                va='center', ha='left', color='#F8FAFC', fontweight='bold')
                
    st.pyplot(fig)
