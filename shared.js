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

  const navbarHTML = `
    <div class="nav-container">
      <a href="/" class="nav-logo">블로그 도구모음</a>
      <ul class="nav-menu">
        <li><a href="/short">단축 링크</a></li>
        <li><a href="/">동물상 테스트</a></li>
        <li><a href="/lotto">로또 통계</a></li>
        <li><a href="/eraser">AI 지우개</a></li>
        <li><a href="/keyword_analyzer">키워드 분석기</a></li>
        <li class="dropdown">
          <a href="#" class="dropbtn">이미지</a>
          <div class="dropdown-content">
            <a href="/compressor">이미지 용량 줄이기</a>
            <a href="/upscaler">이미지 화질 올리기</a>
          </div>
        </li>
        <li><a href="/blog">전문 블로그</a></li>
        <li><a href="/about">소개</a></li>
        <li><a href="/contact">문의하기</a></li>
      </ul>
    </div>`;

  const footerHTML = `
    <div class="footer-container">
      <div class="footer-section">
        <h4>블로그 도구모음</h4>
        <p style="font-size: 0.9rem; color: #bdc3c7;">인공지능 기술을 일상 속의 재미와 정보로 연결하는 창의적인 도구 모음 플랫폼입니다.</p>
      </div>
      <div class="footer-section">
        <h4>주요 도구</h4>
        <ul>
          <li><a href="/short">단축 링크</a></li>
          <li><a href="/">동물상 테스트</a></li>
          <li><a href="/lotto">로또 번호 통계</a></li>
          <li><a href="/blog">전문 블로그</a></li>
        </ul>
      </div>
      <div class="footer-section">
        <h4>고객 지원</h4>
        <ul>
          <li><a href="/about">사이트 소개</a></li>
          <li><a href="/contact">문의하기</a></li>
          <li><a href="/privacy">개인정보처리방침</a></li>
          <li><a href="/terms">이용약관</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 블로그 도구모음. 사용자에게 가치 있는 정보를 제공하기 위해 최선을 다합니다.</p>
    </div>`;

  const navbar = document.querySelector('.navbar');
  if (navbar) {
    navbar.innerHTML = navbarHTML;
  }

  const footer = document.querySelector('footer');
  if (footer) {
    footer.innerHTML = footerHTML;
  }

  // Active link highlighting
  const currentPage = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-menu a');

  navLinks.forEach(link => {
    const linkPage = link.getAttribute('href');
    // Check for exact match or if it's the root path
    if (linkPage === currentPage || (currentPage === '/' && linkPage === 'index.html')) {
      link.classList.add('active');
      // If it's in a dropdown, also highlight the dropdown button
      if (link.closest('.dropdown-content')) {
        link.closest('.dropdown').querySelector('.dropbtn').classList.add('active');
      }
    }
  });
});