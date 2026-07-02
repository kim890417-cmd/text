import os
import re

ROOT = r"c:\Users\User\Documents\GitHub\text"
HEALTH_DIR = os.path.join(ROOT, "health")
UNCATEGORIZED_DIR = os.path.join(ROOT, "uncategorized")

# Define target HTML files
target_files = [
    os.path.join(ROOT, "blog.html"),
    os.path.join(ROOT, "page", "2", "index.html"),
]

# Add active pages under health
if os.path.exists(HEALTH_DIR):
    for slug in os.listdir(HEALTH_DIR):
        file_path = os.path.join(HEALTH_DIR, slug, "index.html")
        if os.path.isfile(file_path):
            target_files.append(file_path)

# Add active page under uncategorized
target_files.append(os.path.join(UNCATEGORIZED_DIR, "단백질-권장량", "index.html"))

# The custom navbar HTML
NAVBAR_HTML = """  <nav class="navbar">
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
      <button id="theme-toggle">테마 변경</button>
    </div>
  </nav>"""

# Custom script for navbar functionality and theme toggle
SCRIPT_HTML = """  <script>
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
      themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('theme', document.body.classList.contains('dark-mode') ? 'dark' : 'light');
      });
    }
    if (localStorage.getItem('theme') === 'dark') document.body.classList.add('dark-mode');

    document.querySelectorAll('.nav-menu a').forEach(link => {
      const dropdown = link.closest('.dropdown');
      if (link.getAttribute('href') === window.location.pathname) {
        link.classList.add('active');
        if (dropdown) dropdown.querySelector('.dropbtn').classList.add('active');
      }
    });
  </script>"""

# Process each file
for file_path in target_files:
    if not os.path.exists(file_path):
        continue
        
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        modified = False
        
        # 1. Inject link stylesheet in head
        if 'href="/style.css"' not in content:
            # Insert before </head>
            content = content.replace("</head>", '  <link href="/style.css" rel="stylesheet">\n</head>')
            modified = True
            
        # 2. Replace the WP/Astra header with custom navbar
        # Find <header ... id="masthead" ...> ... </header><!-- #masthead -->
        header_pattern = r'<header[^>]*id=["\']masthead["\'][^>]*>.*?</header><!-- #masthead -->'
        match = re.search(header_pattern, content, re.DOTALL)
        if match:
            content = re.sub(header_pattern, NAVBAR_HTML, content, flags=re.DOTALL)
            modified = True
            print(f"Replaced header in: {os.path.relpath(file_path, ROOT)}")
        else:
            # Fallback if comment is missing
            header_pattern_no_comment = r'<header[^>]*id=["\']masthead["\'][^>]*>.*?</header>'
            match_nc = re.search(header_pattern_no_comment, content, re.DOTALL)
            if match_nc:
                content = re.sub(header_pattern_no_comment, NAVBAR_HTML, content, flags=re.DOTALL)
                modified = True
                print(f"Replaced header (no comment fallback) in: {os.path.relpath(file_path, ROOT)}")
                
        # 3. Inject script before </body> if not present
        if 'id="theme-toggle"' in content and 'const themeToggle' not in content:
            content = content.replace("</body>", f"{SCRIPT_HTML}\n</body>")
            modified = True
            
        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
                
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print("\nDone! Header replacements completed.")
