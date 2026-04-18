from pathlib import Path
from datasets import load_dataset
from dotenv import dotenv_values

env_file = Path(__file__).resolve().parents[1]/"keys.env"
HF_TOKEN = dotenv_values(env_file).get("HF_TOKEN")

if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN not found in src/keys.env")

ds = load_dataset("mpingale/mental-health-chat-dataset", token=HF_TOKEN)
ds2 = load_dataset("daniel2588/sarcasm", token=HF_TOKEN)

print(ds)
print(ds2)
