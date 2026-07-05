import os
import re

ROOT = r"c:\Users\User\Documents\GitHub\text"
HEALTH_DIR = os.path.join(ROOT, "health")
UNCATEGORIZED_DIR = os.path.join(ROOT, "uncategorized")
PAGE_DIR = os.path.join(ROOT, "page")

# Define target HTML files
target_files = [
    os.path.join(ROOT, "index.html"),
    os.path.join(ROOT, "blog.html"),
    os.path.join(ROOT, "bmi.html"),
    os.path.join(ROOT, "calorie.html"),
    os.path.join(ROOT, "protein.html"),
    os.path.join(ROOT, "water.html"),
    os.path.join(ROOT, "supplement.html"),
    os.path.join(ROOT, "about.html"),
    os.path.join(ROOT, "contact.html"),
    os.path.join(ROOT, "privacy.html"),
    os.path.join(ROOT, "terms.html"),
]

# Add active pages under page/
if os.path.exists(PAGE_DIR):
    for p in os.listdir(PAGE_DIR):
        file_path = os.path.join(PAGE_DIR, p, "index.html")
        if os.path.isfile(file_path):
            target_files.append(file_path)

# Add active pages under health
if os.path.exists(HEALTH_DIR):
    for slug in os.listdir(HEALTH_DIR):
        file_path = os.path.join(HEALTH_DIR, slug, "index.html")
        if os.path.isfile(file_path):
            target_files.append(file_path)

# Add active pages under uncategorized
if os.path.exists(UNCATEGORIZED_DIR):
    for slug in os.listdir(UNCATEGORIZED_DIR):
        file_path = os.path.join(UNCATEGORIZED_DIR, slug, "index.html")
        if os.path.isfile(file_path):
            target_files.append(file_path)

# Add active pages under tag, category, author folders recursively
for folder in ["tag", "category", "author"]:
    dir_path = os.path.join(ROOT, folder)
    if os.path.exists(dir_path):
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file == "index.html":
                    target_files.append(os.path.join(root, file))

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
    </div>
  </nav>"""

# Custom script for navbar functionality (mobile dropdown via JS inline style, not CSS classes)
SCRIPT_HTML = """  <script>
    // Active link highlight
    document.querySelectorAll('.nav-menu a').forEach(link => {
      const dropdown = link.closest('.dropdown');
      if (link.getAttribute('href') === window.location.pathname) {
        link.classList.add('active');
        if (dropdown) dropdown.querySelector('.dropbtn').classList.add('active');
      }
    });

    // Mobile dropdown: JS-driven, not CSS-driven (to avoid Astra theme CSS conflicts)
    const dropbtn = document.querySelector('.dropbtn');
    const dropdownContent = document.querySelector('.dropdown-content');
    const isMobile = () => window.innerWidth <= 600;

    function initDropdown() {
      if (!dropbtn || !dropdownContent) return;
      if (isMobile()) {
        // On mobile: hide dropdown and handle tap toggle
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
        // On desktop: reset to CSS-driven hover
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

      // Tap on a link inside dropdown: allow navigation
      dropdownContent.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', (e) => {
          e.stopPropagation();
        });
      });

      // Close when tapping outside
      document.addEventListener('click', (e) => {
        if (!isMobile()) return;
        if (!dropbtn.contains(e.target) && !dropdownContent.contains(e.target)) {
          dropdownContent.style.setProperty('display', 'none', 'important');
        }
      });
    }
  </script>"""

# Process each file
for file_path in target_files:
    if not os.path.exists(file_path):
        continue
        
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        modified = False
        
        # 1. Inject link stylesheet in head (skip for root/pages if already styled, but keep for consistency)
        if 'href="/style.css"' not in content and 'style.css' not in file_path:
            content = content.replace("</head>", '  <link href="/style.css" rel="stylesheet">\n</head>')
            modified = True
            
        # 2. Replace the WP/Astra header or existing custom navbar
        navbar_pattern = r'  <nav class="navbar">.*?</nav>'
        header_pattern = r'<header[^>]*id=["\']masthead["\'][^>]*>.*?</header><!-- #masthead -->'
        header_pattern_no_comment = r'<header[^>]*id=["\']masthead["\'][^>]*>.*?</header>'
        
        if re.search(navbar_pattern, content, re.DOTALL):
            content = re.sub(navbar_pattern, NAVBAR_HTML, content, flags=re.DOTALL)
            modified = True
            print(f"Updated navbar in: {os.path.relpath(file_path, ROOT)}")
        elif re.search(header_pattern, content, re.DOTALL):
            content = re.sub(header_pattern, NAVBAR_HTML, content, flags=re.DOTALL)
            modified = True
            print(f"Replaced header in: {os.path.relpath(file_path, ROOT)}")
        elif re.search(header_pattern_no_comment, content, re.DOTALL):
            content = re.sub(header_pattern_no_comment, NAVBAR_HTML, content, flags=re.DOTALL)
            modified = True
            print(f"Replaced header (no comment fallback) in: {os.path.relpath(file_path, ROOT)}")
                
        # 3. Replace old script block or inject new one before </body>
        old_script_pattern = r'  <script>\s*const themeToggle = document\.getElementById\(\'theme-toggle\'\);.*?</script>'
        clean_script_pattern = r'  <script>\s*document\.querySelectorAll\(\'\.nav-menu a\'\).*?</script>'
        
        if 'isMobile' not in content:
            if re.search(old_script_pattern, content, re.DOTALL):
                content = re.sub(old_script_pattern, SCRIPT_HTML, content, flags=re.DOTALL)
                modified = True
                print(f"Replaced old theme script in: {os.path.relpath(file_path, ROOT)}")
            elif re.search(clean_script_pattern, content, re.DOTALL):
                content = re.sub(clean_script_pattern, SCRIPT_HTML, content, flags=re.DOTALL)
                modified = True
                print(f"Replaced clean script in: {os.path.relpath(file_path, ROOT)}")
            else:
                # Broader fallback: replace any <script> block that contains theme toggle comment
                any_theme_pattern = r'  <script>\s*// Theme toggle script.*?</script>'
                if re.search(any_theme_pattern, content, re.DOTALL):
                    content = re.sub(any_theme_pattern, SCRIPT_HTML, content, flags=re.DOTALL)
                    modified = True
                    print(f"Replaced legacy theme script in: {os.path.relpath(file_path, ROOT)}")
                elif 'document.querySelectorAll(\'.nav-menu a\')' not in content:
                    content = content.replace("</body>", f"{SCRIPT_HTML}\n</body>")
                    modified = True
                    print(f"Injected script in: {os.path.relpath(file_path, ROOT)}")

        # 4. Remove search widget HTML if present
        search_widget_pattern = r'<aside[^>]*class=["\'][^"\']*widget_search[^"\']*["\'][^>]*>.*?</aside>'
        if re.search(search_widget_pattern, content, re.DOTALL):
            content = re.sub(search_widget_pattern, "", content, flags=re.DOTALL)
            modified = True
            print(f"Removed search widget in: {os.path.relpath(file_path, ROOT)}")
            
        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
                
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print("\nDone! Header replacements completed.")
