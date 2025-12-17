import React, { useState } from 'react';
import styles from './QuizComponent.module.css';

interface Question {
  question: string;
  options: string[];
  correctIndex: number;
  explanation?: string;
}

interface QuizComponentProps {
  questions: Question[];
}

export default function QuizComponent({ questions }: QuizComponentProps): JSX.Element {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null);
  const [showResult, setShowResult] = useState(false);
  const [score, setScore] = useState(0);
  const [answeredQuestions, setAnsweredQuestions] = useState<boolean[]>(
    new Array(questions.length).fill(false)
  );

  const handleAnswerSelect = (index: number) => {
    if (answeredQuestions[currentQuestion]) return;

    setSelectedAnswer(index);
    const newAnswered = [...answeredQuestions];
    newAnswered[currentQuestion] = true;
    setAnsweredQuestions(newAnswered);

    if (index === questions[currentQuestion].correctIndex) {
      setScore(score + 1);
    }
  };

  const handleNext = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
      setSelectedAnswer(null);
    } else {
      setShowResult(true);
    }
  };

  const handlePrevious = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
      setSelectedAnswer(null);
    }
  };

  const handleRestart = () => {
    setCurrentQuestion(0);
    setSelectedAnswer(null);
    setShowResult(false);
    setScore(0);
    setAnsweredQuestions(new Array(questions.length).fill(false));
  };

  const percentage = Math.round((score / questions.length) * 100);

  if (showResult) {
    return (
      <div className={styles.quizContainer}>
        <div className={styles.resultCard}>
          <h2>Quiz Complete!</h2>
          <div className={styles.scoreCircle}>
            <span className={styles.scoreNumber}>{percentage}%</span>
          </div>
          <p className={styles.scoreText}>
            You scored {score} out of {questions.length} questions correctly.
          </p>
          <p className={styles.feedbackText}>
            {percentage >= 80
              ? 'Excellent work! You have a solid understanding of Module 1 concepts.'
              : percentage >= 60
              ? 'Good effort! Review the lessons to strengthen your understanding.'
              : 'Keep studying! Review the lessons and try again.'}
          </p>
          <button className={styles.restartButton} onClick={handleRestart}>
            Retake Quiz
          </button>
        </div>
      </div>
    );
  }

  const question = questions[currentQuestion];
  const isAnswered = answeredQuestions[currentQuestion];
  const isCorrect = selectedAnswer === question.correctIndex;

  return (
    <div className={styles.quizContainer}>
      <div className={styles.progressBar}>
        <div
          className={styles.progressFill}
          style={{ width: `${((currentQuestion + 1) / questions.length) * 100}%` }}
        />
      </div>
      <div className={styles.questionHeader}>
        <span className={styles.questionNumber}>
          Question {currentQuestion + 1} of {questions.length}
        </span>
        <span className={styles.scoreDisplay}>Score: {score}</span>
      </div>
      <div className={styles.questionCard}>
        <h3 className={styles.questionText}>{question.question}</h3>
        <div className={styles.optionsContainer}>
          {question.options.map((option, index) => {
            let optionClass = styles.option;
            if (isAnswered) {
              if (index === question.correctIndex) {
                optionClass = `${styles.option} ${styles.correct}`;
              } else if (index === selectedAnswer && !isCorrect) {
                optionClass = `${styles.option} ${styles.incorrect}`;
              }
            } else if (selectedAnswer === index) {
              optionClass = `${styles.option} ${styles.selected}`;
            }

            return (
              <button
                key={index}
                className={optionClass}
                onClick={() => handleAnswerSelect(index)}
                disabled={isAnswered}
              >
                <span className={styles.optionLetter}>
                  {String.fromCharCode(65 + index)}
                </span>
                {option}
              </button>
            );
          })}
        </div>
        {isAnswered && question.explanation && (
          <div className={styles.explanation}>
            <strong>{isCorrect ? 'Correct!' : 'Incorrect.'}</strong> {question.explanation}
          </div>
        )}
      </div>
      <div className={styles.navigation}>
        <button
          className={styles.navButton}
          onClick={handlePrevious}
          disabled={currentQuestion === 0}
        >
          Previous
        </button>
        <button
          className={styles.navButton}
          onClick={handleNext}
          disabled={!isAnswered}
        >
          {currentQuestion === questions.length - 1 ? 'Finish' : 'Next'}
        </button>
      </div>
    </div>
  );
}
