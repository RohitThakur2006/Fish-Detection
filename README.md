# 🌊 AquaScan // Fish Species Detection System

A cyberpunk-meets-deep-ocean web application for AI fish species identification. Built with a high-performance **FastAPI** backend and an immersive, single-file **cyber-marine frontend** featuring spotlight reveal optics, caustics, sonar scanning, and responsive telemetry.

---

## 🚀 Quick Start

### 1. Start the Backend

Make sure you have Python installed, then install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

Launch the FastAPI development server from the project root:

```bash
uvicorn backend.main:app --reload
```

The API will be live at `http://localhost:8000`:
- **API Documentation (Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Health Check:** [http://localhost:8000/health](http://localhost:8000/health)
- **Supported Species Catalog:** [http://localhost:8000/species](http://localhost:8000/species)
- **Prediction Endpoint:** `POST http://localhost:8000/predict` (multipart form with `file`)

---

### 2. Launch the Frontend

The frontend is a **self-contained, standalone web interface**. You can open it directly in any modern browser:

- Double-click or open [frontend/index.html](file:///c:/Users/jarna/Desktop/projects/ai's/anti/fish/frontend/index.html) in Chrome, Edge, Firefox, or Safari.
- Alternatively, serve it via any static file server:
  ```bash
  python -m http.server 3000 --directory frontend
  ```
  Then visit [http://localhost:3000](http://localhost:3000).

> **Note:** If the backend is not running, the frontend automatically falls back to simulated telemetry so you can preview the complete UI and animations offline.

---

## 🎨 Frontend Features & Inspiration

Inspired by the **Cyber Ronin** design specification (`inspo.md`) and adapted into a bioluminescent ocean aesthetic:

- **Bioluminescent Abyssal Palette:** Deep trench navy (`#030712`, `#071527`), electric cyan (`#00F0FF`), phosphor green (`#00FF9D`), and laser coral (`#FF007F`).
- **Interactive Cursor Spotlight Reveal:** Moving your cursor or touching the screen reveals an alternate bioluminescent deep-sea spectrum via dynamic CSS mask gradients.
- **Pure CSS Caustic Light & Bathymetric Grid:** Shifting underwater light shafts and bathymetric sonar grid lines rendered purely in GPU-accelerated CSS.
- **Micro-Bubble Particle System:** Translucent ocean bubbles rising with randomized drift, delays, and sizes.
- **Cybernetic Scanning Reticle:** High-tech drag-and-drop target zone that sweeps an animated laser beam across the specimen during inference.
- **Dynamic Telemetry & Info Cards:** Shows species name with letter pull-up transitions, confidence gauge bar, top-3 ranked alternatives, collapsible marine habitat/diet metadata, and live stat counters.
- **Underwater Ripple Shader:** SVG displacement filter distorting specimen imagery on hover.
- **Full Responsive Breakpoints:** Custom layouts for desktop (1024px+), tablet (900px, 768px, 720px), and mobile (480px, 360px).

---

## 🔌 Integrating Your Trained Model

The system is designed for **instant model drop-in**:

1. Place your model file (e.g., `fish_model.h5`, `model.onnx`, or `model.pt`) into `backend/model/`.
2. Open [`backend/inference.py`](file:///c:/Users/jarna/Desktop/projects/ai's/anti/fish/backend/inference.py).
3. Replace the mock prediction logic inside `async def predict(image_bytes: bytes)` with your preprocessing (Pillow resize/normalize) and model forward pass:
   ```python
   # Example:
   # image = Image.open(io.BytesIO(image_bytes)).convert('RGB').resize((224, 224))
   # preds = model.predict(np.expand_dims(np.array(image)/255.0, axis=0))
   ```
4. Return the predicted species, confidence, top 3, and species metadata. The frontend automatically displays your model's real outputs!
