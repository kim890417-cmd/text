document.addEventListener('DOMContentLoaded', () => {
  const drawButton = document.getElementById('draw-button');
  const lottoNumbersContainer = document.getElementById('lotto-numbers');
  const themeToggle = document.getElementById('theme-toggle');

  // Lotto number generation logic
  drawButton.addEventListener('click', () => {
    const numbers = [];
    while (numbers.length < 6) {
      const randomNum = Math.floor(Math.random() * 45) + 1;
      if (!numbers.includes(randomNum)) {
        numbers.push(randomNum);
      }
    }

    // Sort numbers in ascending order
    numbers.sort((a, b) => a - b);

    // Display numbers
    lottoNumbersContainer.innerHTML = '';
    numbers.forEach((num, index) => {
      setTimeout(() => {
        const numberElement = document.createElement('div');
        numberElement.classList.add('number');
        numberElement.textContent = num;
        lottoNumbersContainer.appendChild(numberElement);
      }, index * 100); // Staggered animation
    });
  });

  // Theme toggle logic
  themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    
    // Save preference to localStorage (optional but good practice)
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
  });

  // Load saved theme preference
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
  }

  // Comment logic
  const commentForm = document.getElementById('comment-form');
  const commentDisplay = document.getElementById('comment-display');
  const commenterName = document.getElementById('commenter-name');
  const commentText = document.getElementById('comment-text');

  function loadComments() {
    const comments = JSON.parse(localStorage.getItem('comments') || '[]');
    commentDisplay.innerHTML = '';
    comments.forEach(comment => {
      const commentElement = document.createElement('div');
      commentElement.classList.add('comment');
      commentElement.innerHTML = `<strong>${comment.name}</strong>: ${comment.text}`;
      commentDisplay.appendChild(commentElement);
    });
  }

  commentForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = commenterName.value;
    const text = commentText.value;

    const comments = JSON.parse(localStorage.getItem('comments') || '[]');
    comments.push({ name, text });
    localStorage.setItem('comments', JSON.stringify(comments));

    commenterName.value = '';
    commentText.value = '';
    loadComments();
  });

  loadComments();
});
