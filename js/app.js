// 메인 페이지: 단축링크 생성 (Cloudflare Functions 호출)
const form = document.getElementById("shorten-form");
const longUrlInput = document.getElementById("long-url");
const aliasInput = document.getElementById("custom-alias");
const submitBtn = document.getElementById("submit-btn");
const result = document.getElementById("result");
const shortLink = document.getElementById("short-link");
const statsLink = document.getElementById("stats-link");
const copyBtn = document.getElementById("copy-btn");
const errorMsg = document.getElementById("error-msg");

function showError(msg) {
  errorMsg.textContent = msg;
  errorMsg.classList.remove("hidden");
  result.classList.add("hidden");
}

function showResult(code) {
  const url = `${location.origin}/s/${code}`;
  shortLink.textContent = url;
  shortLink.href = url;
  statsLink.href = `/stats.html?code=${encodeURIComponent(code)}`;
  errorMsg.classList.add("hidden");
  result.classList.remove("hidden");
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  errorMsg.classList.add("hidden");

  const longUrl = longUrlInput.value.trim();
  const alias = aliasInput.value.trim();

  submitBtn.disabled = true;
  submitBtn.textContent = "생성 중...";

  try {
    const res = await fetch("/api/shorten", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ url: longUrl, alias }),
    });
    const data = await res.json();

    if (!res.ok) {
      showError(data.error || "오류가 발생했어요.");
      return;
    }
    showResult(data.code);
  } catch (err) {
    console.error(err);
    showError("서버에 연결하지 못했어요. 잠시 후 다시 시도해 주세요.");
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "짧게 만들기";
  }
});

// 복사 버튼
copyBtn.addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(shortLink.textContent);
    copyBtn.textContent = "복사됨!";
    copyBtn.classList.add("copied");
    setTimeout(() => {
      copyBtn.textContent = "복사";
      copyBtn.classList.remove("copied");
    }, 1500);
  } catch {
    showError("복사에 실패했어요. 링크를 직접 선택해 복사해 주세요.");
  }
});
