import streamlit as st

def main():
    st.title("🏆 KUIS SEJARAH AC MILAN 🏆")
    st.markdown("=" * 40)
    st.write("Jawablah pertanyaan berikut dengan benar!\n")

    # Daftar soal (pertanyaan, pilihan, jawaban benar)
    questions = [
        {
            "question": "1. Kapan AC Milan didirikan?",
            "options": ["A. 1899", "B. 1903", "C. 1910", "D. 1920"],
            "answer": "A"
        },
        {
            "question": "2. Siapa pendiri AC Milan?",
            "options": ["A. Paolo Maldini", "B. Herbert Kilpin", "C. Arrigo Sacchi", "D. Silvio Berlusconi"],
            "answer": "B"
        },
        {
            "question": "3. Stadion AC Milan bernama?",
            "options": ["A. Allianz Stadium", "B. Olimpico", "C. San Siro", "D. Maracana"],
            "answer": "C"
        },
        {
            "question": "4. Berapa kali AC Milan menjuarai Liga Champions (hingga 2024)?",
            "options": ["A. 5 kali", "B. 6 kali", "C. 7 kali", "D. 8 kali"],
            "answer": "C"
        },
        {
            "question": "5. Siapa pelatih AC Milan saat meraih Liga Champions 2007?",
            "options": ["A. Carlo Ancelotti", "B. Fabio Capello", "C. Massimiliano Allegri", "D. Stefano Pioli"],
            "answer": "A"
        }
    ]

    score = 0
    user_answers = []

    # Loop pertanyaan
    for q in questions:
        st.subheader(q["question"])
        user_answer = st.radio(
            "Pilih jawaban:",
            q["options"],
            key=q["question"]
        )
        
        # Handle when user selects an answer
        if user_answer == q["options"][0]:
            correct_answer = "A"
        elif user_answer == q["options"][1]:
            correct_answer = "B"
        elif user_answer == q["options"][2]:
            correct_answer = "C"
        elif user_answer == q["options"][3]:
            correct_answer = "D"
        
        user_answers.append((user_answer, correct_answer))
    
    if st.button('Submit'):
        for idx, (user_answer, correct_answer) in enumerate(user_answers):
            q = questions[idx]
            if user_answer == q["answer"]:
                st.success(f"Pertanyaan {idx + 1}: ✅ Benar!")
                score += 1
            else:
                st.error(f"Pertanyaan {idx + 1}: ❌ Salah! Jawaban yang benar adalah {q['answer']}")

        # Menampilkan skor akhir
        st.markdown("=" * 40)
        st.write(f"Skor akhir Anda: {score}/{len(questions)}")
        if score == len(questions):
            st.balloons()
            st.write("🔥 Luar biasa! Anda fans sejati AC Milan!")
        elif score >= 3:
            st.write("👍 Cukup bagus! Tapi bisa lebih baik lagi.")
        else:
            st.write("😅 Masih perlu belajar sejarah AC Milan.")
        st.markdown("=" * 40)

# Jalankan aplikasi Streamlit
if __name__ == "__main__":
    main()
