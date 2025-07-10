# Simple String Reversal API

## Endpoint
**POST** `/reverse`

### ✅ Request JSON
```
{
  "input": "hello"
}
```

### 🔁 Response JSON
```
{
  "reversed": "olleh"
}
```

### ❌ Errors
- Missing input:
```
{"error": "Missing \"input\" in request body"}
```

- Invalid type:
```
{"error": "\"input\" must be a string"}
```

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Access: http://127.0.0.1:5000/reverse
