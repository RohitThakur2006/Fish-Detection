# Fish Species Detection — Project Documentation

## 1. Overview

A web application that allows a user to upload an image of a fish and receive a
prediction of its species. The core of the system is a trained image
classification model (CNN / transfer-learning based) exposed through a
backend API, with a frontend that handles image upload and displays results.

This project is being built as a **college/academic project**. The model
training and dataset are handled separately by the author; this document
focuses on defining the **system architecture, backend, and frontend** so
the model can be integrated cleanly once ready.

---

## 2. Goals

- [ ] Accept a fish image upload from the user (JPG/PNG)
- [ ] Run the image through a trained classification model
- [ ] Return predicted species + confidence score
- [ ] Display results clearly on the frontend
- [ ] (Optional/stretch) Show top-3 predictions instead of just top-1
- [ ] (Optional/stretch) Maintain a history of past predictions
- [ ] (Optional/stretch) Show a short info card about the predicted species (habitat, diet, etc.)

---

## 3. Tech Stack

### Model
- **Format:** `.h5` / `.pt` / `.onnx` (decide based on framework — see note below)
- **Framework used for training:** _TBD by author (PyTorch or TensorFlow/Keras)_
- **Architecture:** Transfer learning recommended (e.g. ResNet50, EfficientNet-B0, MobileNetV2) rather than a CNN trained from scratch, given likely limited dataset size
- **Input size:** _TBD — commonly 224x224_
- **Output:** Softmax probabilities across N fish species classes

> **Note:** Decide PyTorch vs TensorFlow *before* building the backend, since
> the inference code differs. If unsure, TensorFlow/Keras `.h5` models are
> slightly simpler to load and serve in a Python backend with minimal code.
> Exporting to **ONNX** is a good idea either way — it decouples the backend
> from the training framework and is generally faster for inference.

### Backend
- **Framework:** FastAPI (Python)
  - Async support, automatic OpenAPI/Swagger docs, easy to containerize
- **Model serving:** Load model once at startup (not per-request) and keep in memory
- **Image handling:** Pillow (PIL) for preprocessing (resize, normalize)
- **Server:** Uvicorn (ASGI server for FastAPI)

### Frontend
- **Tech stack: not specified here.** The frontend is being built separately
  and can be implemented in any framework, as long as it talks to the
  backend API defined in Section 5.
- What the frontend needs to do (framework-agnostic):
  1. Provide an image upload UI (file picker and/or drag-and-drop)
  2. Send the selected image to the backend via `POST /predict` as `multipart/form-data`
  3. Receive a JSON response containing the predicted species, confidence score, and optionally top-3 predictions
  4. Display the result to the user (species name, confidence %, optionally the uploaded image alongside the result)
  5. Handle basic error/loading states (e.g. no file selected, backend unreachable, prediction failed)
- Since the backend is a plain REST API with CORS enabled, it can be
  consumed by literally any frontend (React, Vue, plain HTML/JS, a no-code
  builder, mobile app, etc.) without backend changes.

### Deployment (for demo/submission)
- **Backend:** Render / Railway / a local server during demo
- **Frontend:** Vercel / Netlify (if React) — trivial free-tier deployment
- **Containerization (optional but good for academic credit):** Docker for backend, to show reproducibility

---

## 4. System Architecture

```
[User Browser]
      |
      | (upload image)
      v
[Frontend - built separately, any stack]
      |
      | POST /predict (multipart/form-data)
      v
[Backend - FastAPI]
      |
      | preprocess image -> run inference
      v
[Model - CNN/Transfer Learning]
      |
      | species + confidence
      v
[Backend returns JSON]
      |
      v
[Frontend displays result]
```

---

## 5. Backend API Design

### `POST /predict`
**Request:** `multipart/form-data` with an image file field (`file`)

**Response:**
```json
{
  "species": "Clownfish",
  "confidence": 0.94,
  "top_3": [
    {"species": "Clownfish", "confidence": 0.94},
    {"species": "Damselfish", "confidence": 0.04},
    {"species": "Angelfish", "confidence": 0.02}
  ]
}
```

### `GET /health`
Simple health check endpoint — useful for demo/deployment verification.

### `GET /species` (optional)
Returns the list of species the model can classify — useful for displaying
supported species on the frontend.

---

## 6. Folder Structure (proposed)

```
fish-species-detector/          (this repo — backend only)
├── backend/
│   ├── main.py              # FastAPI app, routes
│   ├── model/
│   │   └── fish_model.h5    # trained model (added later)
│   ├── inference.py         # preprocessing + prediction logic
│   ├── requirements.txt
│   └── Dockerfile
├── PROJECT.md
└── README.md

frontend/                       (separate project/repo, built independently)
```

---

## 7. Open Questions / To Decide

- [ ] Final model framework: PyTorch or TensorFlow?
- [ ] Number of fish species classes the model supports
- [ ] Max image upload size / accepted formats
- [ ] Will the app run fully online, or is a local demo acceptable for submission?
- [ ] Do you need user accounts / prediction history stored in a database (adds SQLite/Postgres to scope)?
- [ ] Any specific UI requirements from your instructor/rubric (e.g. must show confusion matrix, accuracy metrics, etc. in the app itself)?
- [ ] What domain/port will the frontend run on? (needed to configure CORS correctly on the FastAPI backend)

---

## 8. Milestones (suggested)

1. Set up backend skeleton with a dummy `/predict` endpoint (returns mock data)
2. Set up frontend with image upload + calls dummy endpoint, confirm end-to-end flow works
3. Plug in the real trained model, replace mock logic with real inference
4. Polish UI (loading states, error handling, confidence display)
5. Write documentation, prepare demo, deploy (if required)

---

## 9. Notes

_(Use this space for any decisions, blockers, or changes made during development.)_
