from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class LocalModel:
    def __init__(self, model_name="deepseek-ai/deepseek-coder-1.3b-instruct"):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16,
                device_map="auto",
                trust_remote_code=True
            )
            self.model.eval()
        except Exception as e:
            raise RuntimeError(f"Failed to load model: {str(e)}")

    def generate(self, prompt, max_tokens=512):
        try:
            with torch.no_grad():
                inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
                output = self.model.generate(
                    **inputs,
                    max_new_tokens=max_tokens,
                    pad_token_id=self.tokenizer.eos_token_id
                )
                return self.tokenizer.decode(output[0], skip_special_tokens=True)
        except Exception as e:
            raise RuntimeError(f"Generation failed: {str(e)}")

    def __del__(self):
        if hasattr(self, 'model'):
            del self.model
            if torch.cuda.is_available():
                torch.cuda.empty_cache()