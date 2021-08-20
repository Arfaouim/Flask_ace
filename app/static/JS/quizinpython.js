/* ====== Questions ====== */
let questions = [
    {
      question: 'What is a correct syntax to output "Hello World" in Python?',
      options: [
        'echo("Hello World")',
        'msgBox("Hello World")',
        'msg("Hello World")',
        'print("Hello World")'
      ],
      answer: 3
    },
    {
      question: "How do you insert COMMENTS in Python code?",
      options: [
        "/*This is comment*/",
        "#This is comment",
        "//This is comment"
      ],
      answer: 1
    },
    {
      question: 'Which one is NOT a legal variable name?',
      options: ["_myvar", "Myvar", "my-var", "my_var"],
      answer: 3
    },
    {
      question: "How do you create a variable with the numeric value 5?",
      options: ["x = int(5)", "x = 5", "x == 5", "The two first answers are correct"],
      answer: 3
    },
    {
      question: 'What is the correct file extension for Python files?',
      options: [".pt", ".pyth", ".py", ".pyt"],
      answer: 2
    },
    {
      question: "What is the correct way to create a function in Python?",
      options: ["def myFunction():", "create myFunction():", "function myFunction():"],
      answer: 0
    }
  ];
  /* ======== End ======== */
  
  /* ==== True code ==== */
  const progressBar = document.querySelector(".progress--bar");
  const questionArea = document.querySelector(".questionArea");
  const scoreArea = document.querySelector(".scoreArea");
  const scoreText1 = document.querySelector(".scoreText1");
  const scorePct = document.querySelector(".scorePct");
  
  //initial data
  let currentQuestion = 0;
  let correctAnswers = 0;
  
  showQuestion();
  
  //reset event
  document.querySelector(".scoreArea button").addEventListener("click", () => {
    currentQuestion = 0;
    correctAnswers = 0;
    showQuestion();
  });
  
  //Functions
  function showQuestion() {
    if (questions[currentQuestion]) {
      let q = questions[currentQuestion];
  
      let progress = Math.floor((currentQuestion / questions.length) * 100);
      progressBar.style.width = `${progress}%`;
  
      scoreArea.style.display = "none";
      questionArea.style.display = "block";
  
      document.querySelector(".question").innerHTML = q.question;
  
      let optionsHtml = "";
  
      for (let i in q.options) {
        optionsHtml += `<div data-op="${i}" class="option"><span> ${
          parseInt(i) + 1
        }</span> ${q.options[i]}</div>`;
      }
  
      document.querySelector(".options").innerHTML = optionsHtml;
  
      document.querySelectorAll(".options .option").forEach((item) => {
        item.addEventListener("click", optionsClickEvent);
      });
    } else {
      finishQuiz();
    }
  }
  
  function optionsClickEvent(e) {
    let clickedOption = parseInt(e.target.getAttribute("data-op"));
  
    if (questions[currentQuestion].answer === clickedOption) {
      correctAnswers++;
    }
  
    currentQuestion++;
    showQuestion();
  }
  
  function finishQuiz() {
    let points = Math.floor((correctAnswers / questions.length) * 100);
  
    if (points <= 30) {
      scoreText1.innerHTML = "oops, needs to improve";
      scorePct.style.color = "#f00000";
    } else if (points > 30 && points < 70) {
      scoreText1.innerHTML = "Good job";
      scorePct.style.color = "#ffc900";
    } else if (points > 30 && points >= 70) {
      scoreText1.innerHTML = "Ohh very good, congratulations!";
      scorePct.style.color = "#0d630d";
    }
  
    scorePct.innerHTML = `${points}% Correct`;
    document.querySelector(
      ".scoreText2"
    ).innerHTML = `Out of ${questions.length} you got it ${correctAnswers}`;
  
    scoreArea.style.display = "block";
    questionArea.style.display = "none";
    progressBar.style.width = "100%";
  }
  