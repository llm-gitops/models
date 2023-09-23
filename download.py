import os
from huggingface_hub import snapshot_download

# Fetch environment variables
repo_id = os.environ["MODEL_REPO"]
file_pattern = os.environ["MODEL_FILE"]

snapshot_download(
    repo_id=repo_id,
    allow_patterns=file_pattern,
    local_dir="./model"
)