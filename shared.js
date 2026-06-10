document.addEventListener('DOMContentLoaded', () => {
  // --- Theme Toggle Logic ---
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

  // --- Menu Data ---
  const navLinksData = [
    { href: '/short', text: '단축 링크' },
    { href: '/', text: '동물상 테스트' },
    { href: '/lotto', text: '로또 통계' },
    { 
      text: '이미지 도구',
      isDropdown: true,
      links: [
        { href: '/compressor', text: '이미지 용량 줄이기' },
        { href: '/upscaler', text: '이미지 화질 올리기' },
        { href: '/eraser', text: 'AI 지우개' },
      ]
    },
    { href: '/video_maker', text: 'AI 영상 제작' },
    { href: '/keyword_analyzer', text: '키워드 분석기' },
    { href: '/blog', text: '전문 블로그' },
    { href: '/about', text: '소개' },
    { href: '/contact', text: '문의하기' },
  ];

  const footerLinksData = {
    "주요 도구": [
      { href: '/short', text: '단축 링크' },
      { href: '/', text: '동물상 테스트' },
      { href: '/lotto', text: '로또 번호 통계' },
      { href: '/compressor', text: '이미지 용량 줄이기' },
      { href: '/upscaler', text: '이미지 화질 올리기' },
      { href: '/keyword_analyzer', text: '키워드 분석기' },
    ],
    "고객 지원": [
      { href: '/about', text: '사이트 소개' },
      { href: '/contact', text: '문의하기' },
      { href: '/privacy', text: '개인정보처리방침' },
      { href: '/terms', text: '이용약관' },
    ]
  };

  // --- Generation Functions ---
  const createNavLinks = (links) => {
    let html = '';
    links.forEach(link => {
      if (link.isDropdown) {
        html += `<li class="dropdown">
                   <a href="#" class="dropbtn">${link.text}</a>
                   <div class="dropdown-content">
                     ${link.links.map(sublink => `<a href="${sublink.href}">${sublink.text}</a>`).join('')}
                   </div>
                 </li>`;
      } else {
        html += `<li><a href="${link.href}">${link.text}</a></li>`;
      }
    });
    return html;
  };

  const createFooterLinkSections = (sections) => {
    let html = '';
    for (const [title, links] of Object.entries(sections)) {
      html += `<div class="footer-section"><h4>${title}</h4><ul>`;
      html += links.map(link => `<li><a href="${link.href}">${link.text}</a></li>`).join('');
      html += `</ul></div>`;
    }
    return html;
  };

  // --- HTML Templates ---
  const navbarHTML = `
    <div class="nav-container">
      <a href="/" class="nav-logo">블로그 도구모음</a>
      <ul class="nav-menu">
        ${createNavLinks(navLinksData)}
      </ul>
    </div>`;

  const footerHTML = `
    <div class="footer-container">
      <div class="footer-section">
        <h4>블로그 도구모음</h4>
        <p style="font-size: 0.9rem; color: #bdc3c7;">인공지능 기술을 일상 속의 재미와 정보로 연결하는 창의적인 도구 모음 플랫폼입니다.</p>
      </div>
      ${createFooterLinkSections(footerLinksData)}
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 블로그 도구모음. 사용자에게 가치 있는 정보를 제공하기 위해 최선을 다합니다.</p>
    </div>`;

  // --- DOM Injection ---
  const navbar = document.querySelector('.navbar');
  if (navbar) navbar.innerHTML = navbarHTML;

  const footer = document.querySelector('footer');
  if (footer) footer.innerHTML = footerHTML;

  // --- Active Link Highlighting ---
  const currentPage = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-menu a');

  navLinks.forEach(link => {
    const linkHref = link.getAttribute('href');

    // Handle dropdown links
    if (link.closest('.dropdown-content')) {
        if (linkHref === currentPage) {
            link.classList.add('active');
            // Also activate the main dropdown button
            link.closest('.dropdown').querySelector('.dropbtn').classList.add('active');
        }
    } 
    // Handle regular links
    else if ((linkHref === currentPage) || (currentPage === '/index.html' && linkHref === '/')) {
        link.classList.add('active');
    }
  });
});
