document.addEventListener("DOMContentLoaded", function () {
    const allQuestions = [
        {
            question: "Which famous Indian monument is often called the 'Symbol of Love'?",
            options: ["a) Qutub Minar", "b) Hawa Mahal", "c) Taj Mahal","d) Red Fort"],
            correctAnswer: "c) Taj Mahal"
        },
        {
            question: "What classical dance form originated in the state of Kerala?",
            options: ["a) Kathakali", "b) Bharatanatyam", "c) Odissi","d) Kuchipuci"],
            correctAnswer: "a) Kathakali"
        },
        {
            question: "Which Indian festival is known for the colorful decoration of rangoli and the lighting of oil lamps?",
            options: ["a) Holi", "b) Diwali", "c) Navratri","d) Christmas"],
            correctAnswer: "b) Diwali"
        },
        {
            question: "The famous Ajanta and Ellora Caves are located in which Indian state?",
            options: ["a) Madhya Pradesh", "b) Rajasthan", "c) Maharashtra","d) Karnataka"],
            correctAnswer: "c) Maharashtra"
        },
        {
            question: "Which river is considered sacred in Hinduism and plays a central role in India's cultural and religious heritage?",
            options: ["a) Yamuna", "b) Ganga", "c) Brahmaputra", "d) Godavari"],
            correctAnswer: "b) Ganga"
        },
        {
            question: "The Khajuraho Group of Monuments is renowned for its intricate carvings and temples dedicated to which deity?",
            options: ["a) Lord Shiva", "b) Lord Vishnu", "c) Lord Brahma", "d) Lord Rama"],
            correctAnswer: "a) Lord Shiva"
        },
        {
            question: "Which ancient Indian script, dating back to the 3rd century BCE, played a vital role in the spread of Buddhism?",
            options: ["a) Sanskrit", "b) Pali", "c) Tamil", "d) Urdu"],
            correctAnswer: "b) Pali"
        },
        {
            question: "The Mysore Palace is a prominent historical and cultural attraction located in which Indian state?",
            options: ["a) Karnataka", "b) Tamil Nadu", "c) Kerala", "d) Andhra Pradesh"],
            correctAnswer: "a) Karnataka"
        },
        {
            question: "What is the traditional Indian system of medicine that emphasizes balance in the body's vital energies, known as doshas?",
            options: ["a) Yoga", "b) Ayurveda", "c) Naturopathy", "d)d) Siddha"],
            correctAnswer: "b) Ayurveda"
        },
        {
            question: "The Sun Temple at Konark, famous for its intricate architecture, is dedicated to which Hindu deity?",
            options: ["a) Lord Vishnu", "b) Lord Shiva", "c) Lord Brahma", "d) Lord Surya (Sun God)"],
            correctAnswer: "d) Lord Surya (Sun God)"
        },
        {
            question: "Which city is known as the 'City of Lakes' and is famous for its historic palaces and scenic beauty?",
            options: ["a) Jaipur", "b) Udaipur", "c) Jodhpur", "d) Varanasi"],
            correctAnswer: "b) Udaipur"
        },
        {
            question: "Which state is home to the famous annual Rath Yatra (chariot festival) in Puri, dedicated to Lord Jagannath?",
            options: ["a) Odisha", "b) West Bengal", "c) Bihar", "d) Jharkhand"],
            correctAnswer: "a) Odisha"
        },
        {
            question: "Which ancient Indian epic tells the story of the warrior prince Arjuna and his charioteer, Lord Krishna?",
            options: ["a) Ramayana", "b) Mahabharata", "c) Bhagavad Gita", "d) Rigveda"],
            correctAnswer: "b) Mahabharata"
        },
        {
            question: "The famous 'Gateway of India' in Mumbai was built to commemorate the visit of which British monarch?",
            options: ["a) Queen Victoria", "b) King George V", "c) Queen Elizabeth II","d) King Edward VII"],
            correctAnswer: "b) King George V"
        },
        {
            question: "The traditional art of block printing, known for its colorful and intricate designs, is popular in which Indian state?",
            options: ["a) Rajasthan", "b) Kerala", "c) Punjab","d) Gujarat"],
            correctAnswer: "a) Rajasthan"
        },
        {
            question: "The historic site of Hampi, known for its ruins of temples and palaces, is located in the state of:",
            options: ["a) Andhra Pradesh", "b) Karnataka", "c) Telangana","d) Tamil Nadu"],
            correctAnswer: "b) Karnataka"
        },
        {
            question: "The iconic Mehrangarh Fort, one of India's largest forts, is situated in which city?",
            options: ["a) Jaipur", "b) Jaisalmer", "c) Jodhpur","d) Udaipur"],
            correctAnswer: "c) Jodhpur"
        },
        {
            question: "What is the traditional Indian art of decorating hands and feet with intricate henna designs?",
            options: ["a) Mehndi", "b) Rangoli", "c) Batik","d) Kalamkari"],
            correctAnswer: "a) Mehndi"
        },
        {
            question: "Which Indian state is known for its rich tradition of Kathak dance, often performed in temples and royal courts?",
            options: ["a) Uttar Pradesh", "b) Madhya Pradesh", "c) Rajasthan","d) Bihar"],
            correctAnswer: "a) Uttar Pradesh"
        },
       
        // Add more questions here
    ];

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }

    // Shuffle the allQuestions array randomly
    shuffleArray(allQuestions);

    // Define the number of questions to display
    const numberOfQuestionsToDisplay = 10;

    // Select the first set of questions
    const questions = allQuestions.slice(0, numberOfQuestionsToDisplay);

    let currentQuestionIndex = 0;
    let score = 0;

    const questionNumber = document.querySelector(".question-number");
    const questionText = document.getElementById("question-text");
    const optionButtons = document.querySelectorAll(".option-btn");
    const nextButton = document.getElementById("next-btn");
    const backButton = document.getElementById("back-btn");
    const resultText = document.getElementById("result");

    function startQuiz() {
        // Show the first question
        showQuestion();
    }

    function showQuestion() {
        const currentQuestion = questions[currentQuestionIndex];
        questionNumber.innerText = `Question ${currentQuestionIndex + 1}`; // Update question number
        questionText.innerText = currentQuestion.question;

        // Get the options container element
        const optionsContainer = document.querySelector(".options-container");
        optionsContainer.innerHTML = ""; // Clear previous options

        for (let i = 0; i < currentQuestion.options.length; i++) {
            // Create an option box for each option
            const optionBox = document.createElement("div");
            optionBox.className = "option-box";

            // Create a button for the option
            const optionButton = document.createElement("button");
            optionButton.className = "option-btn";
            optionButton.textContent = currentQuestion.options[i];

            // Add a click event listener to check the answer
            optionButton.addEventListener("click", () => checkAnswer(optionButton.textContent));

            // Append the button to the option box
            optionBox.appendChild(optionButton);

            // Append the option box to the options container
            optionsContainer.appendChild(optionBox);
        }

        // Update button visibility
        updateButtonVisibility();
    }

    function checkAnswer(selectedOption) {
        const correctAnswer = questions[currentQuestionIndex].correctAnswer;

        if (selectedOption === correctAnswer) {
            score++;
        }

        // Move to the next question
        currentQuestionIndex++;

        // Show the next question or results
        if (currentQuestionIndex < questions.length) {
            showQuestion();
        } else {
            showResult();
        }
    }

    function showResult() {
        // Display the user's score
        resultText.innerText = `Your Score: ${score} / ${questions.length}`;

        // Hide the Back and Next buttons
        backButton.style.display = "none";
        nextButton.style.display = "none";
    }

    function updateButtonVisibility() {
        // Show the Back button if not on the first question
        backButton.style.display = currentQuestionIndex > 0 ? "block" : "none";

        // Show the Next button if not on the last question
        nextButton.style.display = currentQuestionIndex < questions.length - 1 ? "block" : "none";
    }

    function goToPreviousQuestion() {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            showQuestion();
        }
    }

    function goToNextQuestion() {
        if (currentQuestionIndex < questions.length - 1) {
            currentQuestionIndex++;
            showQuestion();
        }
    }

    // Add event listeners for Back and Next buttons
    backButton.addEventListener("click", goToPreviousQuestion);
    nextButton.addEventListener("click", goToNextQuestion);

    // Start the quiz
    startQuiz();
});

function redirect_page_2(){
    location.replace('page2.html');
}