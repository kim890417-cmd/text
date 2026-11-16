let indexPromise;
let newestRequest = 0;

async function loadIndex() {
  const response = await fetch('/food-data/index-manifest.json');
  if (!response.ok) throw new Error('Search index unavailable');
  const manifest = await response.json();
  const chunks = new Array(manifest.files.length);
  let nextFile = 0;
  await Promise.all(Array.from({length: 4}, async () => {
    while (nextFile < manifest.files.length) {
      const index = nextFile++;
      const chunk = await fetch('/food-data/' + manifest.files[index]);
      if (!chunk.ok) throw new Error('Search data unavailable');
      chunks[index] = await chunk.json();
    }
  }));
  return chunks.flat();
}

function relevance(row, query) {
  const name = row[0].toLowerCase();
  if (name === query) return 0;
  if (name.startsWith(query)) return 1;
  return 2;
}

onmessage = async event => {
  const {id, q, page = 0, size = 24} = event.data;
  newestRequest = id;
  try {
    if (!indexPromise) indexPromise = loadIndex();
    const index = await indexPromise;
    if (id !== newestRequest) return;
    const found = index.filter(row => (row[0] + ' ' + row[3]).toLowerCase().includes(q));
    found.sort((a, b) => relevance(a, q) - relevance(b, q));
    postMessage({id, total: found.length, rows: found.slice(page * size, (page + 1) * size)});
  } catch {
    indexPromise = null;
    postMessage({id, error: true});
  }
};
