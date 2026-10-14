(() => {
  const form = document.getElementById('standard-weight-form');
  if (!form) return;
  form.addEventListener('submit', event => {
    event.preventDefault();
    const input = document.getElementById('standard-height');
    const height = Number(input.value);
    const error = document.getElementById('standard-weight-error');
    const result = document.getElementById('standard-weight-result');
    error.textContent = '';
    if (!input.value.trim() || !Number.isFinite(height) || height < 100 || height > 250) {
      result.hidden = true;
      error.textContent = '키를 cm 단위의 100~250 사이 숫자로 입력해 주세요.';
      input.setAttribute('aria-invalid', 'true');
      return;
    }
    input.removeAttribute('aria-invalid');
    const meters = height / 100;
    document.getElementById('standard-male').textContent = (meters * meters * 22).toFixed(1) + 'kg';
    document.getElementById('standard-female').textContent = (meters * meters * 21).toFixed(1) + 'kg';
    document.getElementById('standard-formula').textContent = height + 'cm = ' + meters.toFixed(3) + 'm. 키(m)의 제곱에 각각 22와 21을 곱했습니다.';
    result.hidden = false;
  });
})();
