# IT Quiz game (learning 2D collections)

questions = ('Which component is considered the "brain" of the computer where most calculations and processing take place?',
             'What does "IP" stand for in the context of computer networking?',
             'What is the term for a social engineering attack where an attacker sends fraudulent communications disguised as a trusted source to steal sensitive information?',
             'Which cloud service model provides users with fully functional application software over the internet on a subscription basis, eliminating local installation and management?')

options = [("A. Central Processing Unit (CPU)",
            "B. Random Access Memory (RAM)",
            "C. Hard Disk Drive (HDD)",
            "D. Power Supply Unit (PSU)"),
           ("A. Internal Protocol",
            "B. Internet Protocol",
            "C. Information Process",
            "D. Index Path"),
           ("A. Ransomware",
            "B. DDoS Attack",
            "C. Phishing",
            "D. Spoofing"),
           ("A. Infrastructure as a Service (IaaS)",
            "B. Platform as a Service (PaaS)",
            "C. Data as a Service (DaaS)",
            "D. Software as a Service (SaaS)")]

answers = ["A", "B", "C", "D"]
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter your answer (letter only): ").upper()

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! The correct answer: {answers[question_num]}")

    question_num += 1

total_score = score
if total_score <= 2:
    print(f"\nBetter luck next time! Your total score: {total_score}/{question_num}")
else:
    print(f"\nCongratulations! Your total score: {total_score}/{question_num}")