// GET /s/:code  →  원본 URL로 이동(리다이렉트) + 클릭 수 +1
// 예: dream95.com/s/aB3xK

function notFoundHtml() {
  return `<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>링크를 찾을 수 없어요</title>
<style>body{font-family:sans-serif;background:#0f1117;color:#e8eaf0;display:flex;
align-items:center;justify-content:center;height:100vh;margin:0;text-align:center}
a{color:#6c8cff;text-decoration:none;font-weight:600}</style></head>
<body><div><h1 style="font-size:64px;margin:0">🤔</h1>
<p>존재하지 않는 링크예요.</p>
<a href="/short.html">← 단축링크 만들러 가기</a></div></body></html>`;
}

export async function onRequestGet(context) {
  const { params, env } = context;
  const code = params.code;

  if (!env.LINKS) {
    return new Response("KV(LINKS)가 연결되지 않았어요.", { status: 500 });
  }

  const raw = await env.LINKS.get(code);
  if (!raw) {
    return new Response(notFoundHtml(), {
      status: 404,
      headers: { "content-type": "text/html; charset=utf-8" },
    });
  }

  const data = JSON.parse(raw);

  // 클릭 수 증가 (이동을 막지 않도록 백그라운드로 저장)
  data.clicks = (data.clicks || 0) + 1;
  context.waitUntil(env.LINKS.put(code, JSON.stringify(data)));

  return Response.redirect(data.url, 302);
}
