# 🌊 AquaScan // 3D Neural Deep-Sea Biometrics & Species Classifier

An Awwwards-tier, cyberpunk-meets-deep-ocean web application for AI fish species identification. Built with a high-performance **FastAPI** backend and an immersive, full-viewport **Three.js WebGL 3D center stage** inspired by [igloo.inc](https://www.igloo.inc/) and the Cyber Ronin specification.

---

## 🌟 Visual Centerpiece & Features

- **Full-Viewport 3D WebGL Particle System (`Three.js`)**: 3,500+ interactive bioluminescent particles swirling and reacting in real-time to cursor velocity and 3D camera parallax.
- **Center Stage 3D Holographic Theater**: 
  - Concentric counter-rotating HUD reticle rings.
  - Interactive 3D floating glass pedestal with mouse parallax tilt.
  - Animated dual-tone laser scanline sweeping across specimens during analysis.
  - Biometric neural landmark nodes locking onto anatomical features.
  - Real-time viewport mode switches: `[HOLO SCAN]`, `[NEURAL MESH]`, `[BIOLUMINESCENT]`, `[X-RAY SONAR]`.
- **1-Click Preset Specimens**: Test instantly with 8 curated specimens (Clownfish, Lionfish, Blue Tang, Manta Ray, Swordfish, Angelfish, Pufferfish, Seahorse) without needing an image file.
- **Cyber-Acoustic Audio Engine (`Web Audio API`)**: Real-time synthesized laser sweep chirps and deep submarine sonar pings.
- **Telemetry Dossier**: Top-3 probability matrix, confidence gauges, and deep-sea ecology data (diet, depth, IUCN status, sonar acoustics).

---

## 🚀 Quick Start

### 1. Launch the Frontend
Double-click or open [`frontend/index.html`](file:///c:/Users/jarna/Desktop/projects/ai's/anti/fish/frontend/index.html) directly in any browser (Chrome, Edge, Firefox, Safari).

### 2. Start the Backend (Optional for live API inference)
```bash
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```
API endpoints will be live at `http://localhost:8000`:
- Swagger UI docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Prediction endpoint: `POST http://localhost:8000/predict`
