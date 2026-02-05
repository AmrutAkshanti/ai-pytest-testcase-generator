from ai_module import LocalModel
from typing import Optional

_model_instance = None

def build_prompt(function_str: str) -> str:
    return f"""Generate pytest tests for this function. Follow STRICTLY:
1. Use pytest.raises for error cases, not == comparisons
2. Avoid duplicate test functions
3. For math functions:
   - Use integers (10**n) not floats (1en) for large numbers
   - Limit multiplication tests to reasonable sizes (<10**12)
4. Include:
   - Basic cases
   - Edge cases (None, zeros)
   - Invalid inputs
   - Type validation

Function:
{function_str}

Begin test functions:"""

def generate_tests(function_str: str, model: Optional[LocalModel] = None) -> str:
    global _model_instance

    if not function_str.strip():
        raise ValueError("Function string cannot be empty")

    try:
        if model is None:
            if _model_instance is None:
                _model_instance = LocalModel()
            model = _model_instance

        prompt = build_prompt(function_str)
        return model.generate(prompt, max_tokens=1000)

    except Exception as e:
        raise RuntimeError(f"Test generation failed: {str(e)}")