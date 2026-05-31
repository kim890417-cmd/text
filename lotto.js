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
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
  });

  // Load saved theme preference
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
  }
});
