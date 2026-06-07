// GET /api/stats/:code  →  해당 코드의 클릭 통계 반환

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "content-type": "application/json; charset=utf-8" },
  });
}

export async function onRequestGet(context) {
  const { params, env } = context;

  if (!env.LINKS) {
    return json({ error: "KV(LINKS)가 연결되지 않았어요." }, 500);
  }

  const raw = await env.LINKS.get(params.code);
  if (!raw) return json({ error: "존재하지 않는 단축코드예요." }, 404);

  const data = JSON.parse(raw);
  return json({
    code: params.code,
    url: data.url,
    clicks: data.clicks || 0,
    createdAt: data.createdAt || null,
  });
}
