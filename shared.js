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
      <a href="short.html" class="nav-logo">블로그 도구모음</a>
      <ul class="nav-menu">
        <li><a href="short.html">단축 링크</a></li>
        <li><a href="index.html">동물상 테스트</a></li>
        <li><a href="lotto.html">로또 통계</a></li>
        <li><a href="eraser.html">AI 지우개</a></li>
        <li><a href="keyword_analyzer.html">키워드 분석기</a></li>
        <li class="dropdown">
          <a href="#" class="dropbtn">이미지</a>
          <div class="dropdown-content">
            <a href="compressor.html">이미지 용량 줄이기</a>
            <a href="upscaler.html">이미지 화질 올리기</a>
          </div>
        </li>
        <li><a href="blog.html">전문 블로그</a></li>
        <li><a href="about.html">소개</a></li>
        <li><a href="contact.html">문의하기</a></li>
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
          <li><a href="short.html">단축 링크</a></li>
          <li><a href="index.html">동물상 테스트</a></li>
          <li><a href="lotto.html">로또 번호 통계</a></li>
          <li><a href="blog.html">전문 블로그</a></li>
          <li><a href="tools.html">블로그 도구</a></li>
        </ul>
      </div>
      <div class="footer-section">
        <h4>고객 지원</h4>
        <ul>
          <li><a href="about.html">사이트 소개</a></li>
          <li><a href="contact.html">문의하기</a></li>
          <li><a href="privacy.html">개인정보처리방침</a></li>
          <li><a href="terms.html">이용약관</a></li>
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
  const currentPage = window.location.pathname.split('/').pop();
  const navLinks = document.querySelectorAll('.nav-menu a');

  navLinks.forEach(link => {
    const linkPage = link.getAttribute('href');
    if (linkPage === currentPage) {
      link.classList.add('active');
      // If it's in a dropdown, also highlight the dropdown button
      if (link.closest('.dropdown-content')) {
        link.closest('.dropdown').querySelector('.dropbtn').classList.add('active');
      }
    }
  });
});