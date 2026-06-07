// POST /api/shorten  →  단축링크 생성
// Cloudflare KV(이름표: LINKS)에 { url, clicks, createdAt } 저장

const ALPHABET = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789";

function randomCode(len = 5) {
  let code = "";
  const arr = new Uint32Array(len);
  crypto.getRandomValues(arr);
  for (let i = 0; i < len; i++) code += ALPHABET[arr[i] % ALPHABET.length];
  return code;
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "content-type": "application/json; charset=utf-8" },
  });
}

export async function onRequestPost(context) {
  const { request, env } = context;

  // KV 바인딩 확인 (대시보드에서 LINKS 라는 이름으로 연결해야 함)
  if (!env.LINKS) {
    return json({ error: "서버에 KV(LINKS)가 연결되지 않았어요. 설정을 확인하세요." }, 500);
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: "요청 형식이 올바르지 않아요." }, 400);
  }

  let target = (body.url || "").trim();
  const alias = (body.alias || "").trim();

  if (!target) return json({ error: "URL을 입력해 주세요." }, 400);
  if (!/^https?:\/\//i.test(target)) target = "https://" + target;

  let parsed;
  try {
    parsed = new URL(target);
  } catch {
    return json({ error: "올바른 URL 형식이 아니에요." }, 400);
  }

  // 자기 자신 도메인으로의 단축 방지
  if (parsed.host === new URL(request.url).host) {
    return json({ error: "이 사이트 자체 주소는 단축할 수 없어요." }, 400);
  }

  let code;

  if (alias) {
    if (!/^[a-zA-Z0-9_-]+$/.test(alias)) {
      return json({ error: "별칭에는 영문, 숫자, -, _ 만 쓸 수 있어요." }, 400);
    }
    if (alias.length < 2 || alias.length > 64) {
      return json({ error: "별칭은 2~64자로 입력해 주세요." }, 400);
    }
    const exists = await env.LINKS.get(alias);
    if (exists) return json({ error: "이미 사용 중인 별칭이에요." }, 409);
    code = alias;
  } else {
    // 비어있는 코드를 찾을 때까지 시도
    for (let i = 0; i < 6; i++) {
      const c = randomCode(5 + Math.floor(i / 2));
      if (!(await env.LINKS.get(c))) {
        code = c;
        break;
      }
    }
    if (!code) return json({ error: "코드 생성에 실패했어요. 다시 시도해 주세요." }, 500);
  }

  await env.LINKS.put(
    code,
    JSON.stringify({ url: target, clicks: 0, createdAt: Date.now() })
  );

  return json({ code });
}
