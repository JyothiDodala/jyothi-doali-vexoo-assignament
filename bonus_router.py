# ============================================================
# Bonus: Reasoning-Aware Adapter / Smart Query Router
# Vexoo Labs AI Engineer Assignment
# Author: Jyothi Dodali (Upgraded Version)
# ============================================================

from typing import Tuple


# ============================================================
# KEYWORDS
# ============================================================

MATH_KEYWORDS = [
    "calculate", "how many", "total", "percent", "solve",
    "cost", "price", "distance", "speed", "multiply",
    "divide", "sum", "average", "ratio"
]

LEGAL_KEYWORDS = [
    "law", "contract", "clause", "jurisdiction",
    "liability", "court", "regulation", "compliance",
    "rights", "statute", "legal", "attorney"
]

MEDICAL_KEYWORDS = [
    "diagnosis", "treatment", "patient", "disease",
    "symptom", "drug", "hospital", "surgery", "dose"
]


# ============================================================
# QUERY TYPE DETECTION
# ============================================================

def detect_query_type(query: str) -> Tuple[str, float]:
    query_lower = query.lower()

    math_score = sum(1 for kw in MATH_KEYWORDS if kw in query_lower)
    legal_score = sum(1 for kw in LEGAL_KEYWORDS if kw in query_lower)
    medical_score = sum(1 for kw in MEDICAL_KEYWORDS if kw in query_lower)

    scores = {
        "Math Reasoning Module": math_score,
        "Legal Retrieval Module": legal_score,
        "Medical Knowledge Module": medical_score,
    }

    best_module = max(scores, key=scores.get)
    best_score = scores[best_module]

    if best_score == 0:
        return "General Semantic Search", 0.60

    confidence = min(round(best_score / 5, 2), 1.0)
    return best_module, confidence


# ============================================================
# MODULES (REALISTIC RESPONSES)
# ============================================================

def math_module(query: str) -> str:
    return (
        f"🔢 Math Reasoning Activated\n"
        f"Query: {query}\n\n"
        f"Step 1: Extracting numbers...\n"
        f"Step 2: Identifying operation...\n"
        f"Step 3: Performing calculation...\n"
        f"✅ Final Answer: (Simulated result)"
    )


def legal_module(query: str) -> str:
    return (
        f"⚖️ Legal Retrieval Activated\n"
        f"Query: {query}\n\n"
        f"→ Searching legal database...\n"
        f"→ Matching relevant clauses...\n"
        f"→ Providing summarized legal insight...\n"
        f"📄 Result: This query relates to legal compliance and contract law."
    )


def medical_module(query: str) -> str:
    return (
        f"🏥 Medical Knowledge Activated\n"
        f"Query: {query}\n\n"
        f"→ Checking symptoms and conditions...\n"
        f"→ Matching medical guidelines...\n"
        f"💊 Result: Consult a healthcare professional for accurate diagnosis."
    )


def general_module(query: str) -> str:
    return (
        f"🔍 General Semantic Search Activated\n"
        f"Query: {query}\n\n"
        f"→ Running semantic search...\n"
        f"📚 Top Result: Machine Learning is a subset of AI that enables systems to learn from data."
    )


# ============================================================
# ROUTER FUNCTION
# ============================================================

def route_query(query: str):
    module, confidence = detect_query_type(query)

    if "Math" in module:
        response = math_module(query)
    elif "Legal" in module:
        response = legal_module(query)
    elif "Medical" in module:
        response = medical_module(query)
    else:
        response = general_module(query)

    return module, confidence, response


# ============================================================
# MAIN PROGRAM (INTERACTIVE)
# ============================================================

def main():
    print("=" * 60)
    print("🤖 SMART QUERY ROUTER SYSTEM")
    print("=" * 60)

    while True:
        query = input("\n💬 Enter your query (type 'exit' to quit): ")

        if query.lower() == "exit":
            print("👋 Exiting... Thank you!")
            break

        module, confidence, response = route_query(query)

        print("\n" + "=" * 60)
        print("📊 RESULT")
        print("=" * 60)

        print(f"📥 Query       : {query}")
        print(f"🎯 Module      : {module}")
        print(f"📈 Confidence  : {int(confidence * 100)}%")

        print("\n💡 Response:")
        print(response)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()