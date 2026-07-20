import os
import re

repo_path = r'C:\Users\User\Desktop\키워드 글쓰기\healthfit_repo'

# 1. New Formatted Author Section for author archive pages
NEW_AUTHOR_BOX = '''<section class="ast-author-box ast-archive-description" style="display:flex;flex-wrap:wrap;gap:24px;align-items:flex-start;padding:28px;background:#f8fafc;border-radius:12px;margin-bottom:30px;border:1px solid #e2e8f0;">
  <div class="ast-author-avatar" style="flex-shrink:0;">
    <img alt="건강노트 운영자" src="https://healthfit100.com/images/author.jpg" class="avatar avatar-120 photo" height="150" width="150" decoding="async" style="width:140px;height:140px;object-fit:cover;border-radius:50%;box-shadow:0 4px 12px rgba(0,0,0,0.1);border:3px solid #ffffff;">
  </div>
  <div class="ast-author-bio" style="flex:1;min-width:280px;line-height:1.8;color:#334155;">
    <h1 class="page-title ast-archive-title" style="font-size:24px;font-weight:700;margin-bottom:14px;color:#0f172a;">글쓴이 : 건강노트</h1>
    
    <p style="margin-bottom:12px;">저는 2014년에 소위로 임관해 고성, 남양주, 대관령 등 여러 부대를 거치며 군 생활을 했고 대위로 전역했습니다.</p>
    
    <p style="margin-bottom:12px;">전역 후에는 대전에서 스피치 학원과 행사 회사에서 <strong>PD</strong>로 일했습니다. 무대를 만드는 일은 보람찼지만 밤샘이 정말 많았습니다.</p>
    
    <p style="margin-bottom:12px;">군 생활의 강도, PD 시절의 잦은 밤샘, 그리고 나이가 더해지면서 어느 순간부터 <strong>몸이 눈에 띄게 약해졌습니다.</strong> 작은 일에도 쉽게 지치고, 주변에서 <em>"몸 좀 챙기라"</em>는 잔소리도 참 많이 들었습니다. 그때부터 영양제 하나, 음식 하나도 그냥 먹지 않고 <strong>"이게 정말 나에게 맞나"</strong>를 찾아보기 시작했습니다.</p>
    
    <p style="margin-bottom:12px;">다행히 저는 혼자가 아니었습니다. 대학에서 <strong>식품학</strong>을 전공한 덕분에 영양 성분표를 읽고 자료를 해석하는 데 익숙했고, 영양사나 건강 분야에서 일하는 학과 친구들이 주변에 많았습니다. 게다가 <strong>매제(여동생 남편)가 의사</strong>라서 궁금한 점을 물어볼 수 있었고, 가깝게 지내는 <strong>약사 형</strong>과도 약과 영양제 이야기를 자주 나눴습니다.</p>
    
    <p style="margin-bottom:0;">이렇게 보고 듣고 공부한 것을, 저처럼 몸이 약해 고민하는 분들을 위해 하나씩 정리한 것이 <strong>건강노트</strong>입니다.</p>
  </div>
</section>'''

# Apply to author pages
author_files = [
    os.path.join(repo_path, 'author', 'kim890417', 'index.html'),
    os.path.join(repo_path, 'author', 'kim890417', 'page', '2', 'index.html'),
    os.path.join(repo_path, 'author', 'kim890417', 'page', '3', 'index.html'),
]

author_box_regex = re.compile(r'<section class="ast-author-box ast-archive-description">.*?</section>', re.DOTALL)

for af in author_files:
    if os.path.exists(af):
        with open(af, 'r', encoding='utf-8') as f:
            content = f.read()
        if author_box_regex.search(content):
            content = author_box_regex.sub(NEW_AUTHOR_BOX, content)
            with open(af, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'[DONE] Updated author page: {af}')

# 2. Update about.html
about_file = os.path.join(repo_path, 'about.html')
if os.path.exists(about_file):
    with open(about_file, 'r', encoding='utf-8') as f:
        about_content = f.read()

    # Update story section with photo & line breaks
    OLD_STORY = '''<h2>제가 건강을 공부하게 된 이야기</h2>
        <p>저는 2014년에 소위로 임관해 고성, 남양주, 대관령 등 여러 부대를 거치며 군 생활을 했고 대위로 전역했습니다. 전역 후에는 대전에서 스피치 학원과 행사 회사에서 <strong>PD</strong>로 일했습니다. 무대를 만드는 일은 보람찼지만 밤샘이 정말 많았습니다.</p>
        <p>군 생활의 강도, PD 시절의 잦은 밤샘, 그리고 나이가 더해지면서 어느 순간부터 <strong>몸이 눈에 띄게 약해졌습니다.</strong> 작은 일에도 쉽게 지치고, 주변에서 "몸 좀 챙기라"는 잔소리도 참 많이 들었습니다. 그때부터 영양제 하나, 음식 하나도 그냥 먹지 않고 "이게 정말 나에게 맞나"를 찾아보기 시작했습니다.</p>
        <p>다행히 저는 혼자가 아니었습니다. 대학에서 <strong>식품학</strong>을 전공한 덕분에 영양 성분표를 읽고 자료를 해석하는 데 익숙했고, 영양사나 건강 분야에서 일하는 학과 친구들이 주변에 많았습니다. 게다가 <strong>매제(여동생 남편)가 의사</strong>라서 궁금한 점을 물어볼 수 있었고, 가깝게 지내는 <strong>약사 형</strong>과도 약과 영양제 이야기를 자주 나눴습니다. 이렇게 보고 듣고 공부한 것을, 저처럼 몸이 약해 고민하는 분들을 위해 하나씩 정리한 것이 건강노트입니다.</p>'''

    NEW_STORY = '''<h2>제가 건강을 공부하게 된 이야기</h2>
        <div style="display:flex;flex-wrap:wrap;gap:20px;align-items:flex-start;margin-top:20px;margin-bottom:20px;">
          <img src="https://healthfit100.com/images/author.jpg" alt="건강노트 운영자" style="width:140px;height:140px;object-fit:cover;border-radius:50%;box-shadow:0 4px 12px rgba(0,0,0,0.1);border:3px solid #ffffff;flex-shrink:0;">
          <div style="flex:1;min-width:260px;line-height:1.8;">
            <p style="margin-bottom:12px;">저는 2014년에 소위로 임관해 고성, 남양주, 대관령 등 여러 부대를 거치며 군 생활을 했고 대위로 전역했습니다.</p>
            <p style="margin-bottom:12px;">전역 후에는 대전에서 스피치 학원과 행사 회사에서 <strong>PD</strong>로 일했습니다. 무대를 만드는 일은 보람찼지만 밤샘이 정말 많았습니다.</p>
            <p style="margin-bottom:12px;">군 생활의 강도, PD 시절의 잦은 밤샘, 그리고 나이가 더해지면서 어느 순간부터 <strong>몸이 눈에 띄게 약해졌습니다.</strong> 작은 일에도 쉽게 지치고, 주변에서 <em>"몸 좀 챙기라"</em>는 잔소리도 참 많이 들었습니다. 그때부터 영양제 하나, 음식 하나도 그냥 먹지 않고 <strong>"이게 정말 나에게 맞나"</strong>를 찾아보기 시작했습니다.</p>
            <p style="margin-bottom:12px;">다행히 저는 혼자가 아니었습니다. 대학에서 <strong>식품학</strong>을 전공한 덕분에 영양 성분표를 읽고 자료를 해석하는 데 익숙했고, 영양사나 건강 분야에서 일하는 학과 친구들이 주변에 많았습니다. 게다가 <strong>매제(여동생 남편)가 의사</strong>라서 궁금한 점을 물어볼 수 있었고, 가깝게 지내는 <strong>약사 형</strong>과도 약과 영양제 이야기를 자주 나눴습니다.</p>
            <p style="margin-bottom:0;">이렇게 보고 듣고 공부한 것을, 저처럼 몸이 약해 고민하는 분들을 위해 하나씩 정리한 것이 <strong>건강노트</strong>입니다.</p>
          </div>
        </div>'''

    if OLD_STORY in about_content:
        about_content = about_content.replace(OLD_STORY, NEW_STORY, 1)
        with open(about_file, 'w', encoding='utf-8') as f:
            f.write(about_content)
        print('[DONE] Updated about.html')
    else:
        print('[WARN] OLD_STORY pattern not exact match in about.html')
