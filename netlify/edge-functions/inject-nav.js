export default async (request, context) => {
  const response = await context.next();

  const contentType = response.headers.get('content-type') || '';
  if (!contentType.includes('text/html')) return response;

  let html = await response.text();

  const cssBlock = `
  <link rel="stylesheet" href="/style.css">
  <style>
    #masthead, .ast-above-header-bar, .ast-below-header-bar,
    .main-header-bar, .main-header-bar-wrap { display: none !important; }
  </style>`;

  const navBlock = `
  <nav class="navbar">
    <div class="nav-container">
      <a href="/" class="nav-logo">블로그 도구모음</a>
      <ul class="nav-menu">
        <li><a href="/short">단축링크</a></li>
        <li class="dropdown">
          <a href="#" class="dropbtn">이미지 도구</a>
          <div class="dropdown-content">
            <a href="/compressor">이미지 용량 줄이기</a>
            <a href="/upscaler">이미지 화질 올리기</a>
            <a href="/eraser">AI 지우개</a>
          </div>
        </li>
        <li><a href="/keyword_analyzer">키워드 분석기</a></li>
        <li><a href="/blog">전문 블로그</a></li>
        <li><a href="/about">소개</a></li>
        <li><a href="/contact">문의하기</a></li>
      </ul>
      <button id="theme-toggle">테마 변경</button>
    </div>
  </nav>
  <script>
    const t = document.getElementById('theme-toggle');
    if (t) t.addEventListener('click', () => {
      document.body.classList.toggle('dark-mode');
      localStorage.setItem('theme', document.body.classList.contains('dark-mode') ? 'dark' : 'light');
    });
    if (localStorage.getItem('theme') === 'dark') document.body.classList.add('dark-mode');
  </script>`;

  html = html.replace('</head>', cssBlock + '\n</head>');
  html = html.replace(/(<body[^>]*>)/, '$1\n' + navBlock);

  return new Response(html, {
    status: response.status,
    headers: response.headers,
  });
};
