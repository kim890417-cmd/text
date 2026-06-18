export async function onRequest(context) {
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
      <a href="/" class="nav-logo">건강노트</a>
      <ul class="nav-menu">
        <li class="dropdown">
          <a href="#" class="dropbtn">건강 계산기</a>
          <div class="dropdown-content">
            <a href="/bmi">BMI 계산기</a>
            <a href="/calorie">칼로리 계산기</a>
            <a href="/protein">단백질 계산기</a>
          </div>
        </li>
        <li><a href="/blog">건강 블로그</a></li>
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
}
