(() => {
  'use strict';
  const element = id => document.getElementById(id);
  const escape = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[char]));
  const labels = {
    kcal: ['열량', 'kcal', 'AMT_NUM1'], protein: ['단백질', 'g', 'AMT_NUM3'],
    fat: ['지방', 'g', 'AMT_NUM4'], carbs: ['탄수화물', 'g', 'AMT_NUM6'],
    sugar: ['당류', 'g', 'AMT_NUM7'], fiber: ['식이섬유', 'g', 'AMT_NUM8'], sodium: ['나트륨', 'mg', 'AMT_NUM13']
  };
  const cache = new Map();
  const embedded = parent !== window;
  const pageSize = 24;
  let worker, page = 0, request = 0, rows = [], total = 0;
  const number = value => {
    if (value == null || String(value).trim() === '') return null;
    const parsed = Number(String(value).replaceAll(',', ''));
    return Number.isFinite(parsed) && parsed >= 0 ? parsed : null;
  };
  const format = value => value == null ? '미제공' : Number(value.toFixed(2)).toLocaleString('ko-KR');
  if (embedded) {
    document.querySelector('.home').hidden = true;
    document.querySelector('.catalog-site-nav').hidden = true;
  }
  function search(reset = true) {
    if (reset) page = 0;
    const query = element('query').value.trim();
    request++;
    element('results').replaceChildren();
    element('prev').disabled = true;
    element('next').disabled = true;
    element('page').textContent = '';
    if (!query) {
      rows = [];
      total = 0;
      element('status').textContent = '음식명이나 제품명을 입력해 주세요. 예: 쌀밥, 닭가슴살, 두부';
      return;
    }
    element('status').textContent = '식품을 찾고 있어요. 처음 검색할 때는 자료를 준비하는 시간이 필요합니다.';
    if (!worker) {
      worker = new Worker('/food-search-worker.js?v=20261101');
      worker.onerror = () => {
        element('status').textContent = '검색 자료를 읽지 못했습니다. 다시 검색해 주세요.';
        worker.terminate();
        worker = null;
      };
      worker.onmessage = event => {
        if (event.data.id !== request) return;
        if (event.data.error) {
          element('status').textContent = '영양정보를 불러오지 못했습니다. 다시 검색해 주세요.';
          return;
        }
        rows = event.data.rows;
        total = event.data.total;
        render();
      };
    }
    worker.postMessage({id: request, q: query.toLowerCase(), page, size: pageSize});
  }
  function render() {
    element('status').textContent = '검색 결과 ' + total.toLocaleString('ko-KR') + '건';
    element('results').innerHTML = rows.map((row, index) => '<button class="card" data-item="' + index + '"><div class="body"><small>' + escape(row[4]) + '</small><h2>' + escape(row[0]) + '</h2><p>' + escape(row[3] || '공식 식품 영양정보') + '</p><small>기준량 확인하고 먹을 양 계산하기 →</small></div></button>').join('') || '<p>검색 결과가 없습니다. 제품명 일부나 재료명으로 다시 찾아보세요.</p>';
    element('page').textContent = (total ? page + 1 : 0) + ' / ' + Math.ceil(total / pageSize);
    element('prev').disabled = page === 0;
    element('next').disabled = (page + 1) * pageSize >= total;
  }
  function nutrition(values, factor = 1) {
    return '<div class="nutrients">' + Object.entries(labels).map(([key, [label, unit]]) => '<p>' + label + '<br><strong>' + format(values[key] == null ? null : values[key] * factor) + '</strong> ' + unit + '</p>').join('') + '</div>';
  }
  async function detail(index) {
    const selected = rows[index];
    if (!selected) return;
    try {
      let records = cache.get(selected[2]);
      if (!records) {
        const response = await fetch('/food-data/foods-' + selected[2] + '.json');
        if (!response.ok) throw new Error('Food data unavailable');
        records = await response.json();
        cache.set(selected[2], records);
        if (cache.size > 6) cache.delete(cache.keys().next().value);
      }
      const food = records.find(record => record.FOOD_CD === selected[1]);
      if (!food) throw new Error('Food not found');
      const values = Object.fromEntries(Object.entries(labels).map(([key, label]) => [key, number(food[label[2]])]));
      const basis = String(food.SERVING_SIZE || '');
      const match = basis.match(/^\s*(\d+(?:\.\d+)?)\s*g\s*$/i);
      const grams = match ? Number(match[1]) : null;
      const canCalculate = grams > 0;
      element('detailBody').innerHTML = '<small>' + escape(food.DB_GRP_NM) + ', ' + escape(food.FOOD_CD) + '</small><h2>' + escape(food.FOOD_NM_KR) + '</h2><p>' + escape(food.MAKER_NM || '') + '</p><p>표시 기준량 <strong>' + escape(basis || '미제공') + '</strong></p>' + (canCalculate ? '<label class="quantity">먹을 양 <input id="grams" type="number" value="' + grams + '" min="0.1" max="5000" step="any"> g</label><p>먹을 양을 바꾸면 아래 영양성분도 같은 비율로 계산합니다.</p>' : '<p>g 단위의 기준량이 없어 중량 환산을 제공하지 않습니다.</p>') + '<div id="nutrition">' + nutrition(values) + '</div><p class="notice">자료 출처 ' + escape(food.SUB_REF_NAME || '식품의약품안전처') + '<br>데이터 기준일 ' + escape(food.UPDATE_DATE || '미제공') + '<br>미제공 값은 빈 정보로 유지합니다. 실제 제품 표시와 조리 상태도 함께 확인해 주세요.</p>' + (embedded && canCalculate ? '<div class="actions"><button id="addFood" class="primary">내 식품에 저장</button><button id="addMeal">식사 기록에 담기</button></div>' : '');
      if (canCalculate) {
        const amount = () => {
          const value = Number(element('grams').value);
          return Number.isFinite(value) && value > 0 && value <= 5000 ? value : null;
        };
        element('grams').oninput = () => {
          const value = amount();
          element('nutrition').innerHTML = value ? nutrition(values, value / grams) : '<p>0보다 크고 5,000g 이하로 입력해 주세요.</p>';
        };
        if (embedded) {
          const send = type => {
            const value = amount();
            if (!value) return;
            const payload = {name: food.FOOD_NM_KR, code: food.FOOD_CD, source: '식품의약품안전처 ' + food.FOOD_CD + ', 원본 ' + basis + ', ' + (food.UPDATE_DATE || ''), nutrients: Object.fromEntries(Object.entries(values).map(([key, nutrient]) => [key, nutrient == null ? null : nutrient * 100 / grams])), grams: value};
            parent.document.dispatchEvent(new CustomEvent('health-food-import', {detail: {type, payload}}));
            element('detail').close();
          };
          element('addFood').onclick = () => send('food');
          element('addMeal').onclick = () => send('foodMeal');
        }
      }
      element('detail').showModal();
      element('detail').scrollTop = 0;
    } catch {
      element('status').textContent = '상세정보를 불러오지 못했습니다. 다시 선택해 주세요.';
    }
  }
  element('close').onclick = () => element('detail').close();
  element('results').onclick = event => {
    const button = event.target.closest('[data-item]');
    if (button) detail(Number(button.dataset.item));
  };
  element('search').onsubmit = event => {event.preventDefault(); search();};
  element('prev').onclick = () => {if (page > 0) {page--; search(false);}};
  element('next').onclick = () => {if ((page + 1) * pageSize < total) {page++; search(false);}};
  document.querySelectorAll('[data-query]').forEach(button => button.onclick = () => {element('query').value = button.dataset.query; search();});
  element('query').value = new URLSearchParams(location.search).get('q') || '';
  search();
})();
