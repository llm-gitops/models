from huggingface_hub import snapshot_download
snapshot_download(
	repo_id="TheBloke/vicuna-13B-v1.5-16K-GGML",
	allow_patterns="vicuna-13b-v1.5-16k.ggmlv3.q4_1.bin",
	local_dir="./model")
