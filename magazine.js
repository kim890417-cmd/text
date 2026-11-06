(() => {
  const input = document.querySelector('#article-search');
  if (!input) return;
  const cards = [...document.querySelectorAll('.category-section .story')];
  const groups = [...document.querySelectorAll('.category-section')];
  const status = document.querySelector('#search-status');
  const filterArticles = () => {
    const terms = input.value.trim().toLocaleLowerCase('ko').split(/\s+/).filter(Boolean);
    let shown = 0;
    for (const card of cards) {
      const text = card.textContent.toLocaleLowerCase('ko');
      card.hidden = !terms.every(term => text.includes(term));
      if (!card.hidden) shown++;
    }
    for (const group of groups) group.hidden = ![...group.querySelectorAll('.story')].some(card => !card.hidden);
    status.textContent = terms.length ? (shown ? `${shown}편의 글을 찾았습니다. 아래 글 목록에서 확인하세요.` : '검색 결과가 없습니다. 다른 단어나 짧은 키워드로 검색해 보세요.') : '제목과 글 소개에서 검색합니다.';
  };
  input.addEventListener('input', filterArticles);
  document.querySelector('#article-search-clear')?.addEventListener('click', () => {
    input.value = '';
    filterArticles();
    input.focus();
  });
  filterArticles();
})();
