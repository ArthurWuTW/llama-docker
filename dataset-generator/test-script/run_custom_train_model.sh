llamafactory-cli chat \
    --model_name_or_path google/gemma-2b \
    --preprocessing_num_workers 16 \
    --finetuning_type lora \
    --template default \
    --adapter_name_or_path saves/Gemma-2B/lora/train_2024-09-08-04-56-04 \
    --max_length 5000 \
    --max_new_tokens 5000
