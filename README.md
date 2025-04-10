## VDR_Backend

`VDR_Backend` is a hybrid backend project that integrates **Django** for database and admin management and **Flask** for video/image processing. The whole environment is containerized using **Docker** and orchestrated via `docker-compose`.

---

### 📁 Project Structure Overview

```
VDR_Backend/
├── application/          # Django app: handles models, serializers, views
├── main/                 # Django project: settings, urls, WSGI
├── reviews/              # Django app: reviews functionality
├── web_camera.py         # Flask app for webcam/video processing
├── Dockerfile            # Docker configuration for Flask
├── docker-compose.yml    # Orchestrates Flask and Django services
├── requirements.txt      # Python dependencies
├── manage.py             # Django CLI entry point
└── .env                  # Environment variables
```

---

### 🚀 How to Run the Project (with Docker)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vision-Soft-AI/VDR_Backend.git
   cd VDR_Backend
   ```

2. **Create `.env` file** (if not already):
   ```
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```

3. **Build and run Docker containers:**
   ```bash
   docker-compose up --build
   ```

4. **Access the services:**
   - Django Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)
   - Flask API (webcam service): [http://localhost:5000/](http://localhost:5000/)

---

### ⚙️ Available Services

- **Django Admin Panel:** `/admin/`
- **Django API:** `/api/` *(if exposed via `urls.py`)*
- **Flask Webcam Stream:** served from `web_camera.py` (example: `/video_feed` or `/detect`)
- **Django Apps:**
  - `application`: main models, views, and serializers
  - `reviews`: custom app for user-generated feedback

---

### 🔧 Docker Services (from `docker-compose.yml`)

```yaml
services:
  django:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
    volumes:
      - .:/app

  flask:
    build:
      context: .
    command: python web_camera.py
    ports:
      - "5000:5000"
```

---

### 🧪 Run Tests

```bash
docker-compose exec django python manage.py test
```

---

### 📚 Requirements

Python 3.10+

```txt
Django>=4.2
djangorestframework
opencv-python
numpy
Flask
```

Install locally with:

```bash
pip install -r requirements.txt
```

---

### 📎 Related URLs (in-project links)

- Django settings: `main/settings.py`
- Flask logic: `web_camera.py`
- Serializers: `application/serializers.py`
- Migrations: `application/migrations/`

---
