const URL = "https://teachablemachine.withgoogle.com/models/4yps9I5lk/";

let model, labelContainer, maxPredictions;

// Load the image model
async function init() {
  const modelURL = URL + "model.json";
  const metadataURL = URL + "metadata.json";

  model = await tmImage.load(modelURL, metadataURL);
  maxPredictions = model.getTotalClasses();
  labelContainer = document.getElementById("label-container");
}

// Handle image upload and prediction
async function handleImageUpload(event) {
  const file = event.target.files[0] || event.dataTransfer.files[0];
  if (!file || !file.type.startsWith('image/')) return;

  const reader = new FileReader();
  reader.onload = async (e) => {
    const imgElement = document.getElementById('image-preview');
    imgElement.src = e.target.result;
    imgElement.style.display = 'block';
    document.getElementById('upload-label').style.display = 'none';
    
    document.getElementById('loading-spinner').style.display = 'block';
    document.getElementById('result-container').style.display = 'none';

    // Wait for image to load to predict
    imgElement.onload = async () => {
      await predict(imgElement);
    };
  };
  reader.readAsDataURL(file);
}

// Run the image through the model
async function predict(imgElement) {
  const prediction = await model.predict(imgElement);
  
  document.getElementById('loading-spinner').style.display = 'none';
  document.getElementById('result-container').style.display = 'block';
  
  // Sort predictions by probability
  prediction.sort((a, b) => b.probability - a.probability);
  
  const topResult = prediction[0];
  document.getElementById('result-message').innerText = `당신은 ${topResult.className}상!`;

  labelContainer.innerHTML = '';
  for (let i = 0; i < maxPredictions; i++) {
    const p = prediction[i];
    const percent = (p.probability * 100).toFixed(0);
    
    const barHtml = `
      <div class="result-item">
        <span class="class-name">${p.className}</span>
        <div class="progress-bar-container">
          <div class="progress-bar" style="width: ${percent}%"></div>
        </div>
        <span class="percent-text">${percent}%</span>
      </div>
    `;
    labelContainer.innerHTML += barHtml;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  init();

  const imageInput = document.getElementById('image-input');
  const uploadArea = document.getElementById('upload-area');

  imageInput.addEventListener('change', handleImageUpload);

  // Drag and drop events
  uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragover');
  });

  uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
  });

  uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragover');
    handleImageUpload(e);
  });
});
