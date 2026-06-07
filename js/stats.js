// 통계 페이지: 단축코드의 클릭 수 조회 (Cloudflare Functions 호출)
const form = document.getElementById("stats-form");
const codeInput = document.getElementById("code-input");
const resultBox = document.getElementById("stats-result");
const errorBox = document.getElementById("stats-error");

const clickCount = document.getElementById("click-count");
const statShort = document.getElementById("stat-short");
const statOriginal = document.getElementById("stat-original");
const statCreated = document.getElementById("stat-created");

function showError(msg) {
  errorBox.textContent = msg;
  errorBox.classList.remove("hidden");
  resultBox.classList.add("hidden");
}

function formatDate(ms) {
  if (!ms) return "—";
  return new Date(ms).toLocaleString("ko-KR", {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

// 숫자 카운트업 애니메이션
function animateCount(el, target) {
  const duration = 600;
  const start = performance.now();
  function tick(now) {
    const p = Math.min((now - start) / duration, 1);
    el.textContent = Math.round(p * target).toLocaleString("ko-KR");
    if (p < 1) requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
}

async function lookup(rawCode) {
  // 전체 URL을 붙여넣어도 코드만 추출
  let code = rawCode.trim();
  try {
    if (/^https?:\/\//i.test(code)) {
      const parts = new URL(code).pathname.replace(/^\/+|\/+$/g, "").split("/");
      code = parts[0] === "s" ? parts[1] : parts[0];
    }
  } catch {
    /* 그대로 사용 */
  }

  if (!code) {
    showError("단축코드를 입력해 주세요.");
    return;
  }

  try {
    const res = await fetch(`/api/stats/${encodeURIComponent(code)}`);
    const data = await res.json();

    if (!res.ok) {
      showError(data.error || "조회에 실패했어요.");
      return;
    }

    const url = `${location.origin}/s/${data.code}`;
    statShort.textContent = url;
    statShort.href = url;
    statOriginal.textContent = data.url;
    statCreated.textContent = formatDate(data.createdAt);

    errorBox.classList.add("hidden");
    resultBox.classList.remove("hidden");
    animateCount(clickCount, data.clicks || 0);
  } catch (err) {
    console.error(err);
    showError("서버에 연결하지 못했어요. 잠시 후 다시 시도해 주세요.");
  }
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  lookup(codeInput.value);
});

// URL에 ?code=... 가 있으면 자동 조회 (생성 페이지에서 넘어온 경우)
const params = new URLSearchParams(location.search);
const preset = params.get("code");
if (preset) {
  codeInput.value = preset;
  lookup(preset);
}
