document.addEventListener('DOMContentLoaded', () => {
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      document.body.classList.toggle('dark-mode');
      const isDarkMode = document.body.classList.contains('dark-mode');
      localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
    });
  }

  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
  }
});
