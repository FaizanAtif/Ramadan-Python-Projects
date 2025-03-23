import streamlit as st
import random
import time

st.title("📝 Quiz Application")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
    {
        "question": "Which is the national flower of Pakistan?",
        "options": ["Rose", "Tulip", "Jasmine", "Sunflower"],
        "answer": "Jasmine"
    },
    {
        "question": "Which is the highest mountain in Pakistan?",
        "options": ["Nanga Parbat", "Broad Peak", "K2", "Rakaposhi"],
        "answer": "K2"
    },
    {
        "question": "What is the name of Pakistan’s national anthem?",
        "options": ["Sohni Dharti", "Dil Dil Pakistan", "Qaumi Tarana", "Jeevay Jeevay Pakistan"],
        "answer": "Qaumi Tarana"
    },
    {
        "question": "Which year did Pakistan become an independent country?",
        "options": ["1940", "1945", "1947", "1950"],
        "answer": "1947"
    },
    {
        "question": "Who was the first Prime Minister of Pakistan?",
        "options": ["Liaquat Ali Khan", "Zulfikar Ali Bhutto", "Benazir Bhutto", "Muhammad Ali Jinnah"],
        "answer": "Liaquat Ali Khan"
    },
    {
        "question": "Which desert is located in Pakistan?",
        "options": ["Thar Desert", "Sahara Desert", "Kalahari Desert", "Gobi Desert"],
        "answer": "Thar Desert"
    },
    {
        "question": "Which is the longest river in Pakistan?",
        "options": ["Ravi", "Chenab", "Jhelum", "Indus"],
        "answer": "Indus"
    },
    {
        "question": "Who is known as the poet of the East?",
        "options": ["Faiz Ahmed Faiz", "Mirza Ghalib", "Allama Iqbal", "Habib Jalib"],
        "answer": "Allama Iqbal"
    },
    {
        "question": "What is the national sport of Pakistan?",
        "options": ["Cricket", "Hockey", "Football", "Squash"],
        "answer": "Hockey"
    },
    {
        "question": "Which Pakistani city is famous for its historical Badshahi Mosque?",
        "options": ["Karachi", "Islamabad", "Lahore", "Peshawar"],
        "answer": "Lahore"
    },
    {
        "question": "What is the name of the sea bordering Pakistan?",
        "options": ["Arabian Sea", "Red Sea", "Caspian Sea", "Mediterranean Sea"],
        "answer": "Arabian Sea"
    },
    {
        "question": "Which province of Pakistan is the largest by area?",
        "options": ["Punjab", "Sindh", "Balochistan", "Khyber Pakhtunkhwa"],
        "answer": "Balochistan"
    },
    {
        "question": "Which Pakistani scientist won the Nobel Prize in Physics?",
        "options": ["Dr. Abdul Qadeer Khan", "Dr. Abdus Salam", "Dr. Samar Mubarakmand", "Dr. Atta-ur-Rahman"],
        "answer": "Dr. Abdus Salam"
    },
    {
        "question": "What does the white color in Pakistan’s flag represent?",
        "options": ["Peace", "Muslim majority", "Minorities", "Agriculture"],
        "answer": "Minorities"
    },
    {
        "question": "Which Pakistani city is known as the ‘Manchester of Pakistan’?",
        "options": ["Karachi", "Lahore", "Faisalabad", "Multan"],
        "answer": "Faisalabad"
    }
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

selected_option = st.radio("Choose your answer", question["options"], key="answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect! the correct answer is " + question["answer"])
  
    time.sleep(5)
    st.session_state.current_question = random.choice(questions)
    st.rerun()