def ask_question(question, correct_answer, score):
    print(question)
    user_answer = input("Your answer: ")

    cleaned_answer = user_answer.strip().lower()
    cleaned_correct = correct_answer.strip().lower()

    if cleaned_answer == cleaned_correct:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was: {correct_answer}\n")

    return score

def main():
    print("🧠 GENERAL KNOWLEDGE QUIZ 🧠\n")

    score = 0

    score = ask_question("1. What is the capital of France?", "Paris", score)
    score = ask_question("2. What is the largest planet in our solar system?", "Jupiter", score)
    score = ask_question("3. Who wrote the theory of relativity?", "Einstein", score)

    print("🏁 Quiz Over!")
    print(f"Your final score: {score}/3")

if __name__ == "__main__":
    main()