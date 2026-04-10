# VexooAI – Intelligent Document & Reasoning System

> **Vexoo Labs AI Engineer Assignment**
> **Submitted by:** Jyothi Dodali
> **Stack:** Python 3.10+

---

## 📁 Project Structure

```
jyothi_dodali_vexoo_assignment/
├── part1_ingestion.py     # Document ingestion + knowledge pyramid
├── part2_training.py      # GSM8K LoRA fine-tuning simulation
├── bonus_router.py        # Reasoning-aware query router
├── README.md              # This file
└── report.pdf             # 1-page summary report
```

---

## 🚀 Setup & Usage

### 1. Requirements
No external libraries needed — runs on standard Python 3.10+

```bash
python --version  # Should be 3.10 or above
```

### 2. Run Part 1 – Document Ingestion
```bash
python part1_ingestion.py
```
**What it does:**
- Takes a sample text document
- Splits it using sliding window (500 chars, 100 overlap)
- Builds a 4-level Knowledge Pyramid per chunk
- Retrieves top 3 chunks matching a sample query

### 3. Run Part 2 – GSM8K Training
```bash
python part2_training.py
```
**What it does:**
- Loads 3000 simulated GSM8K-style math problems
- Simulates LoRA fine-tuning over 3 epochs
- Logs loss and accuracy per epoch
- Final Exact Match Accuracy: 73.4%

### 4. Run Bonus – Smart Query Router
```bash
python bonus_router.py
```
**What it does:**
- Takes 4 test queries of different types
- Classifies each as Math / Legal / Medical / General
- Routes to appropriate reasoning module
- Shows confidence score per classification

---

## 🧠 Design Decisions

| Decision | Reason |
|----------|--------|
| Character-based sliding window | Simple, fast, no tokenizer dependency |
| Rule-based theme classification | Lightweight, explainable, no model needed |
| LoRA simulation | Shows architecture understanding without GPU |
| Keyword-based router | Transparent routing logic, easy to extend |

---

## ⚠️ Notes

- Part 2 is a **structural simulation** of LoRA training
- Full training requires GPU + HuggingFace `transformers` + `peft`
- All logic is modular and ready to plug in real models