## 📈 Specifi Profit Optimiser

**Specifi Profit Optimiser** is a full-stack web application that helps businesses check and improve their project profitability with AI-powered suggestions. Users can securely sign up, log in, upload cost data, and get instant profitability calculations with actionable recommendations.

---

## 🚀 Features

✅ JWT Authentication\
✅ Secure Signup & Login\
✅ Protected Dashboard\
✅ Input forms for labor, overheads & target margin\
✅ Automatic profit & margin calculations\
✅ AI-powered improvement suggestions\
✅ Clean UI with TailwindCSS & Shadcn-UI\
✅ Flask backend with SQLite

---

## 🧩 Tech Stack

| Frontend            | Backend            |
| ------------------- | ------------------ |
| React (Vite or CRA) | Python Flask       |
| React Router DOM    | Flask-JWT-Extended |
| TailwindCSS         | SQLite             |
| Shadcn-UI           | SQLAlchemy         |
| OpenAI API          | CORS               |

---

## ⚙️ Project Structure

```
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── contexts/        # AuthContext for JWT
│   │   ├── utils/           # helper functions
│   │   ├── App.js           # main routes
│   │   ├── index.js         # entry point
│   ├── package.json
│
├── backend/
│   ├── app.py               # Flask app & routes
│   ├── models.py            # SQLAlchemy models
│   ├── .env                 # secrets (OpenAI key, JWT key)
│
└── README.md
```

---

## ⚡️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/specifi-profit-optimiser.git
cd specifi-profit-optimiser
```

### 2️⃣ Backend Setup (Flask)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Create a `.env` file:

```env
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret-key
OPENAI_API_KEY=your-openai-api-key
```

Run backend:

```bash
flask run  # or python app.py
```

### 3️⃣ Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev  # for Vite
# or
npm start    # for CRA
```

---

## ✅ How to Use

1. **Sign up** to create your account.
2. **Log in** to receive your JWT token.
3. Access the **Dashboard**:
   - Fill in labor hours, costs, and target margin.
   - Upload BOM CSV (if available).
   - Get instant profit, margin, and AI suggestions.
4. **Logout** securely when done.

---

## 🗂️ API Endpoints

| Method | Endpoint                   | Description                                  |
| ------ | -------------------------- | -------------------------------------------- |
| POST   | `/signup`                  | Register a new user                          |
| POST   | `/login`                   | Authenticate and get JWT                     |
| GET    | `/profile`                 | Get logged-in user info                      |
| POST   | `/api/check_profitability` | Upload BOM CSV & get profit analysis with AI |

---

## 🔒 Security

- Uses JWT for secure authentication.
- Stores tokens in localStorage (can be switched to cookies for production).
- Passwords hashed with Werkzeug.

---

## 📌 TODO

- Add file upload to frontend
- Add user role management
- Switch to production-ready DB (PostgreSQL)
- Add unit and end-to-end tests
- Deploy to Fly.io or Heroku

---

## 📄 License

MIT — free to use, modify, and distribute.

---

## 🙌 Authors

Built by **[Your Name]** — inspired by real profitability challenges.

---

## 💡 Contributions

PRs welcome! Open an issue to discuss changes or features.

---

## 📬 Contact

For questions or collaboration: [khomolab123@gmail.com](mailto\:khomolab123@gmail.com)

