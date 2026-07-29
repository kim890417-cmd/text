export async function onRequest(context) {
  const response = await context.next();

  const contentType = response.headers.get('content-type') || '';
  if (!contentType.includes('text/html')) return response;

  let html = await response.text();

  html = html
    .replace(/<link\s+rel=["'](?:icon|apple-touch-icon)["'][^>]*>\s*/gi, '')
    .replace(/<meta\s+name=["']msapplication-TileImage["'][^>]*>\s*/gi, '');

  const cssBlock = `
  <link rel="stylesheet" href="/style.css">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <style id="healthfit-common-shell">
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
            <a href="/water">물 섭취량 계산기</a>
            <a href="/supplement">영양제 권장량</a>
          </div>
        </li>
        <li><a href="/blog">건강 블로그</a></li>
        <li><a href="/about">소개</a></li>
        <li><a href="/contact">문의하기</a></li>
      </ul>
    </div>
  </nav>
  <script>
    // Mobile dropdown toggle script (same as static pages)
    const dropbtn = document.querySelector('.dropbtn');
    const dropdownContent = document.querySelector('.dropdown-content');
    const isMobile = () => window.innerWidth <= 600;

    function initDropdown() {
      if (!dropbtn || !dropdownContent) return;
      if (isMobile()) {
        dropdownContent.style.setProperty('display', 'none', 'important');
        dropdownContent.style.position = 'absolute';
        dropdownContent.style.top = '100%';
        dropdownContent.style.left = '50%';
        dropdownContent.style.transform = 'translateX(-50%)';
        dropdownContent.style.zIndex = '999999';
        dropdownContent.style.background = 'var(--card-bg, #fff)';
        dropdownContent.style.boxShadow = '0 8px 16px rgba(0,0,0,0.15)';
        dropdownContent.style.borderRadius = '8px';
        dropdownContent.style.padding = '10px 0';
        dropdownContent.style.minWidth = '180px';
        dropbtn.style.display = 'inline-block';
      } else {
        dropdownContent.style.removeProperty('display');
        dropdownContent.style.position = '';
        dropbtn.style.display = '';
      }
    }

    initDropdown();
    window.addEventListener('resize', initDropdown);

    if (dropbtn && dropdownContent) {
      dropbtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        if (!isMobile()) return;
        const isOpen = dropdownContent.style.display !== 'none';
        dropdownContent.style.setProperty('display', isOpen ? 'none' : 'block', 'important');
      });

      dropdownContent.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', (e) => {
          e.stopPropagation();
        });
      });

      document.addEventListener('click', (e) => {
        if (!isMobile()) return;
        if (!dropbtn.contains(e.target) && !dropdownContent.contains(e.target)) {
          dropdownContent.style.setProperty('display', 'none', 'important');
        }
      });
    }
  </script>`;

  if (!html.includes('id="healthfit-common-shell"')) {
    html = html.replace('</head>', cssBlock + '\n</head>');
  }
  if (!html.includes('class="navbar"') && !html.includes('class=\'navbar\'')) {
    html = html.replace(/(<body[^>]*>)/, '$1\n' + navBlock);
  }

  const headers = new Headers(response.headers);
  headers.delete('content-length');
  headers.delete('content-encoding');
  headers.delete('etag');

  return new Response(html, {
    status: response.status,
    headers,
  });
}
