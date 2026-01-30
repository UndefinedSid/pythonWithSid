
# 🐍 Python Virtual Environment & pip 

## 1️⃣ macOS me `pip` / `pip3` error kyun aata hai?

macOS me Python **Homebrew se install hota hai**, aur wo system Python ko protect karta hai.

Isliye ye commands ❌ fail hoti hain:

```bash
pip install xyz
pip3 install xyz
```

Error:

```text
externally-managed-environment
```

👉 Matlab: **system Python ke andar packages install allowed nahi hai**

---

## 2️⃣ Solution: Virtual Environment (BEST PRACTICE)

Virtual environment ek **alag Python world** hota hai
Jisme hum safely packages install kar sakte hain.

### Virtual environment create karo

```bash
python3 -m venv .venv
```

### Activate karo

```bash
source .venv/bin/activate
```

Terminal me ye dikhna chahiye:

```text
(.venv)
```

👉 iska matlab: venv ON hai ✅

---

## 3️⃣ Python & pip check karna

```bash
python --version
pip --version
```

Dono `.venv` ke andar hone chahiye.

---

## 4️⃣ Packages install karne ka SAHI tareeka

❌ Galat:

```bash
pip -m install django
python -m install django
```

✅ Sahi:

```bash
python -m pip install django
python -m pip install pymongo
```

🧠 Rule yaad rakho:

```text
python jisse run kar rahe ho,
pip bhi usi python ka use kare
```

---

## 5️⃣ `pip install mongodb` kyun fail hua?

```bash
pip install mongodb
```

❌ Kyunki:

* MongoDB ek **database software** hai
* Python package ka naam **mongodb nahi hota**

✅ Python driver ka naam hai:

```bash
pip install pymongo
```

---

## 6️⃣ Installed packages dekhna

```bash
pip list
```

Example:

```text
Django
pymongo
dnspython
sqlparse
pip
```

---

## 7️⃣ Requirements file banana (IMPORTANT)

❌ Galat:

```bash
pip list > requirement.txt
```

✅ Sahi (industry standard):

```bash
pip freeze > requirements.txt
```

---

## 8️⃣ Future me same packages install karna

```bash
pip install -r requirements.txt
```

---

## 9️⃣ Package uninstall karna

```bash
pip uninstall pymongo
pip uninstall asgiref
```

---

## 🔟 Virtual environment band karna

```bash
deactivate
```

---

## 🧠 Golden Rules (Yaad Rakho)

✔ Har project ka alag venv
✔ `sudo pip` kabhi use mat karo
✔ macOS me global install mat karo
✔ Pehle venv activate karo
✔ Hamesha `python -m pip` use karo

---

## ✅ Perfect Daily Workflow

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install package
python app.py
deactivate
```

---

