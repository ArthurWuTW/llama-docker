llamafactory-cli chat \
    --model_name_or_path meta-llama/Meta-Llama-3-8B \
    --preprocessing_num_workers 16 \
    --quantization_bit 8 \
    --finetuning_type lora \
    --template default \
    --adapter_name_or_path saves/LLaMA3-8B/lora/train_2024-10-20-15-34-15 \
    --max_length 5000 \
    --max_new_tokens 5000
