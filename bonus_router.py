# ============================================================
# Bonus: Reasoning-Aware Adapter / Smart Query Router
# Vexoo Labs AI Engineer Assignment
# Author: Jyothi Dodali
# ============================================================

# ---- Imports ----
from typing import Tuple


# ============================================================
# ROUTING LOGIC
# Detects query type using keyword classification
# Routes to appropriate reasoning module
# ============================================================

# Keyword sets per domain
MATH_KEYWORDS    = ["calculate", "how many", "total", "percent",
                    "solve", "cost", "price", "distance", "speed",
                    "multiply", "divide", "sum", "average", "ratio"]

LEGAL_KEYWORDS   = ["law", "contract", "clause", "jurisdiction",
                    "liability", "court", "regulation", "compliance",
                    "rights", "statute", "legal", "attorney"]

MEDICAL_KEYWORDS = ["diagnosis", "treatment", "patient", "disease",
                    "symptom", "drug", "hospital", "surgery", "dose"]


def detect_query_type(query: str) -> Tuple[str, float]:
    """
    Classifies query into Math / Legal / Medical / General.
    Returns (module_name, confidence_score).
    """
    query_lower = query.lower()

    # Count keyword matches per category
    math_score    = sum(1 for kw in MATH_KEYWORDS    if kw in query_lower)
    legal_score   = sum(1 for kw in LEGAL_KEYWORDS   if kw in query_lower)
    medical_score = sum(1 for kw in MEDICAL_KEYWORDS if kw in query_lower)

    scores = {
        "Math Reasoning Module":    math_score,
        "Legal Retrieval Module":   legal_score,
        "Medical Knowledge Module": medical_score,
    }

    best_module = max(scores, key=scores.get)
    best_score  = scores[best_module]

    # If no keywords matched → General semantic search
    if best_score == 0:
        return "General Semantic Search", 0.60

    # Normalize confidence (max possible ~5 keywords matched)
    confidence = min(round(best_score / 5, 2), 1.0)
    return best_module, confidence


# ============================================================
# MODULE HANDLERS
# Each module simulates a specialized reasoning response
# ============================================================

def math_module(query: str) -> str:
    """Symbolic step-by-step math reasoning."""
    return (
        "🔢 Math Reasoning Activated\n"
        "   → Parsing numerical values from query...\n"
        "   → Identifying operation type (arithmetic / algebra)...\n"
        "   → Executing step-by-step symbolic solver...\n"
        "   → Returning structured chain-of-thought answer."
    )


def legal_module(query: str) -> str:
    """Structured legal document retrieval + citation."""
    return (
        "⚖️  Legal Retrieval Activated\n"
        "   → Searching legal knowledge base...\n"
        "   → Matching relevant statutes and clauses...\n"
        "   → Ranking by jurisdictional relevance...\n"
        "   → Returning structured answer with citations."
    )


def medical_module(query: str) -> str:
    """Medical knowledge base lookup."""
    return (
        "🏥 Medical Knowledge Activated\n"
        "   → Searching clinical database...\n"
        "   → Cross-referencing symptoms and diagnoses...\n"
        "   → Applying evidence-based guidelines...\n"
        "   → Returning diagnosis pathway suggestion."
    )


def general_module(query: str) -> str:
    """General semantic search fallback."""
    return (
        "🔍 General Semantic Search Activated\n"
        "   → Encoding query into vector embedding...\n"
        "   → Running cosine similarity search...\n"
        "   → Retrieving top-k relevant documents...\n"
        "   → Returning ranked semantic results."
    )


# ============================================================
# MAIN ROUTER
# ============================================================

def route_query(query: str):
    """
    Full routing pipeline:
    Query → Classifier → Module → Response
    """
    print(f"\n{'='*60}")
    print(f"  SMART QUERY ROUTER")
    print(f"{'='*60}")
    print(f"\n📥 Query: '{query}'")

    # Detect module
    module, confidence = detect_query_type(query)
    print(f"🎯 Detected Module : {module}")
    print(f"📊 Confidence      : {int(confidence * 100)}%")

    # Route to appropriate handler
    print(f"\n💬 Response:")
    if "Math"    in module: print(math_module(query))
    elif "Legal" in module: print(legal_module(query))
    elif "Medical" in module: print(medical_module(query))
    else:                   print(general_module(query))


# ============================================================
# ENTRY POINT — Test with sample queries
# ============================================================

if __name__ == "__main__":
    test_queries = [
        "Calculate the total cost if I buy 5 items at $12 each with 10% discount",
        "What are the liability clauses in a standard employment contract?",
        "What is the recommended treatment dosage for hypertension?",
        "Tell me about the history of machine learning"
    ]

    for query in test_queries:
        route_query(query)
        print()