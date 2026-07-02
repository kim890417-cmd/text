import os
import re

ROOT = r"c:\Users\User\Documents\GitHub\text"
HEALTH_DIR = os.path.join(ROOT, "health")
UNCATEGORIZED_DIR = os.path.join(ROOT, "uncategorized")

# Define target HTML files
target_files = [
    os.path.join(ROOT, "index.html"),
    os.path.join(ROOT, "blog.html"),
    os.path.join(ROOT, "page", "2", "index.html"),
    os.path.join(ROOT, "bmi", "index.html"),
    os.path.join(ROOT, "calorie", "index.html"),
    os.path.join(ROOT, "protein", "index.html"),
    os.path.join(ROOT, "water", "index.html"),
    os.path.join(ROOT, "supplement", "index.html"),
    os.path.join(ROOT, "about", "index.html"),
    os.path.join(ROOT, "contact", "index.html"),
    os.path.join(ROOT, "privacy", "index.html"),
    os.path.join(ROOT, "terms", "index.html"),
]

# Add active pages under health
if os.path.exists(HEALTH_DIR):
    for slug in os.listdir(HEALTH_DIR):
        file_path = os.path.join(HEALTH_DIR, slug, "index.html")
        if os.path.isfile(file_path):
            target_files.append(file_path)

# Add active page under uncategorized
target_files.append(os.path.join(UNCATEGORIZED_DIR, "단백질-권장량", "index.html"))

# Clean recommended adsense script
CLEAN_ADSENSE_SCRIPT = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3406696816625207" crossorigin="anonymous"></script>'

# Pattern to match any existing adsense script tags with ca-pub-3406696816625207
adsense_pattern = r'<script[^>]*src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-3406696816625207[^"]*"[^>]*></script>'

for file_path in target_files:
    if not os.path.exists(file_path):
        continue
        
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        modified = False
        
        # Check if the tag with our pub ID exists
        match = re.search(adsense_pattern, content)
        if match:
            # Replace existing tag with clean tag
            content = re.sub(adsense_pattern, CLEAN_ADSENSE_SCRIPT, content)
            modified = True
            print(f"Cleaned AdSense code in: {os.path.relpath(file_path, ROOT)}")
        else:
            # If not present at all, insert it before </head>
            if 'ca-pub-3406696816625207' not in content:
                content = content.replace("</head>", f"  {CLEAN_ADSENSE_SCRIPT}\n</head>")
                modified = True
                print(f"Injected AdSense code in: {os.path.relpath(file_path, ROOT)}")
                
        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
                
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print("\nDone! AdSense script tags unified and cleaned.")
