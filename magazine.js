(() => {
  const input = document.querySelector('#article-search');
  if (!input) return;
  const cards = [...document.querySelectorAll('.category-section .story')];
  const groups = [...document.querySelectorAll('.category-section')];
  const status = document.querySelector('#search-status');
  input.addEventListener('input', () => {
    const terms = input.value.trim().toLocaleLowerCase('ko').split(/\s+/).filter(Boolean);
    let shown = 0;
    for (const card of cards) {
      const text = card.textContent.toLocaleLowerCase('ko');
      card.hidden = !terms.every(term => text.includes(term));
      if (!card.hidden) shown++;
    }
    for (const group of groups) group.hidden = ![...group.querySelectorAll('.story')].some(card => !card.hidden);
    status.textContent = terms.length ? `${shown}편의 글을 찾았습니다.` : '';
  });
})();
