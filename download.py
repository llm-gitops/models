from huggingface_hub import snapshot_download
# snapshot_download(
#	repo_id="TheBloke/vicuna-13B-v1.5-16K-GGML",
#	allow_patterns="vicuna-13b-v1.5-16k.ggmlv3.q4_1.bin",
#	local_dir="./model")
snapshot_download(
	repo_id="TheBloke/Llama-2-7b-Chat-GGUF",
	allow_patterns="llama-2-7b-chat.Q5_K_M.gguf",
	local_dir="./model")
