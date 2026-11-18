(() => {
  const input = document.querySelector('#article-search');
  if (!input) return;
  const cards = [...document.querySelectorAll('.category-section .story')];
  const groups = [...document.querySelectorAll('.category-section')];
  const status = document.querySelector('#search-status');

  const getNonSearchElements = () => [
    document.querySelector('.home-purpose'),
    document.querySelector('.purpose-categories'),
    document.querySelector('.home-top'),
    document.querySelector('#tools'),
    document.querySelector('.home-brand-tagline')
  ].filter(Boolean);

  const filterArticles = () => {
    const terms = input.value.trim().toLocaleLowerCase('ko').split(/\s+/).filter(Boolean);
    const isSearching = terms.length > 0;
    let shown = 0;

    for (const card of cards) {
      const text = card.textContent.toLocaleLowerCase('ko');
      card.hidden = !terms.every(term => text.includes(term));
      if (!card.hidden) shown++;
    }
    for (const group of groups) {
      group.hidden = ![...group.querySelectorAll('.story')].some(card => !card.hidden);
    }

    // 검색 중일 때는 검색창 바로 아래에 결과만 오도록 중간 고정 섹션(소개, 카테고리, 최신/추천글, 계산기도구) 강제 숨김
    for (const el of getNonSearchElements()) {
      el.hidden = isSearching;
      el.style.setProperty('display', isSearching ? 'none' : '', 'important');
    }

    status.textContent = isSearching 
      ? (shown ? `${shown}편의 글을 찾았습니다.` : '검색 결과가 없습니다. 다른 단어나 짧은 키워드로 검색해 보세요.') 
      : '제목과 글 소개에서 검색합니다.';
  };

  input.addEventListener('input', filterArticles);
  document.querySelector('#article-search-clear')?.addEventListener('click', () => {
    input.value = '';
    filterArticles();
    input.focus();
  });
  filterArticles();
})();


// ==========================================================================
// 한국인 맞춤 SNS 공유 유틸리티 (Web Share API, 링크 복사, 카카오톡, 네이버, 밴드, X, 페이스북)
// ==========================================================================
(function() {
  function showToast(message) {
    let toast = document.getElementById('sns-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'sns-toast';
      toast.className = 'sns-toast';
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.classList.add('show');
    clearTimeout(toast._timeout);
    toast._timeout = setTimeout(() => {
      toast.classList.remove('show');
    }, 2000);
  }

  function getPageMeta(btn) {
    const bar = btn ? btn.closest('.sns-share-bar') : null;
    const canonical = document.querySelector('link[rel="canonical"]');
    const url = (bar && bar.dataset.url) || (canonical && canonical.href) || window.location.href;
    let title = (bar && bar.dataset.title) || document.title;
    if (title.includes('|')) {
      title = title.split('|')[0].trim();
    }
    return { url, title, domain: window.location.hostname };
  }

  window.snsShare = function(platform, btn) {
    const { url, title, domain } = getPageMeta(btn);
    const encUrl = encodeURIComponent(url);
    const encTitle = encodeURIComponent(title);

    switch (platform) {
      case 'share':
        if (navigator.share) {
          navigator.share({ title: title, url: url }).catch(() => {});
        } else {
          window.snsShare('copy', btn);
        }
        break;

      case 'copy':
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).then(() => {
            showToast('링크가 복사되었습니다');
          }).catch(() => {
            legacyCopy(url, '링크가 복사되었습니다');
          });
        } else {
          legacyCopy(url, '링크가 복사되었습니다');
        }
        break;

      case 'kakao':
        if (window.Kakao && window.Kakao.isInitialized && window.Kakao.isInitialized()) {
          try {
            window.Kakao.Share.sendDefault({
              objectType: 'feed',
              content: {
                title: title,
                description: document.querySelector('meta[name="description"]')?.content || title,
                imageUrl: document.querySelector('meta[property="og:image"]')?.content || '',
                link: { mobileWebUrl: url, webUrl: url }
              }
            });
          } catch (e) {
            fallbackKakao(url);
          }
        } else {
          fallbackKakao(url);
        }
        break;

      case 'naver':
        window.open(
          'https://share.naver.com/web/shareView?url=' + encUrl + '&title=' + encTitle,
          '_blank',
          'width=600,height=500,noopener,noreferrer'
        );
        break;

      case 'band':
        window.open(
          'https://band.us/plugin/share?body=' + encodeURIComponent(title + '\n' + url) + '&route=' + encodeURIComponent(domain),
          '_blank',
          'width=600,height=650,noopener,noreferrer'
        );
        break;

      case 'twitter':
        window.open(
          'https://twitter.com/intent/tweet?text=' + encTitle + '&url=' + encUrl,
          '_blank',
          'width=600,height=450,noopener,noreferrer'
        );
        break;

      case 'facebook':
        window.open(
          'https://www.facebook.com/sharer/sharer.php?u=' + encUrl,
          '_blank',
          'width=600,height=500,noopener,noreferrer'
        );
        break;
    }
  };

  function fallbackKakao(url) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(() => {
        showToast('링크가 복사되었습니다. 카카오톡에 붙여넣으세요');
      }).catch(() => {
        legacyCopy(url, '링크가 복사되었습니다. 카카오톡에 붙여넣으세요');
      });
    } else {
      legacyCopy(url, '링크가 복사되었습니다. 카카오톡에 붙여넣으세요');
    }
  }

  function legacyCopy(text, msg) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand('copy');
      showToast(msg || '링크가 복사되었습니다');
    } catch (e) {
      alert('주소를 복사할 수 없습니다: ' + text);
    }
    document.body.removeChild(ta);
  }
})();
