export CUDA_VISIBLE_DEVICES=1

python run.py \
    --overwrite_output_dir \
    --do_train \
    --do_eval \
    --do_predict \
    --evaluate_during_training \
    --model_name_or_path xlm-roberta-large \
    --few_shot_type prompt \
    --num_k 16 \
    --max_steps -1 \
    --eval_steps 100 \
    --per_device_train_batch_size 64 \
    --learning_rate 2e-5 \
    --num_train_epochs 10 \
    --data_dir data \
    --output_dir result \
    --seed 42 \
    --template "*cls*A_*mask*_translation_of_*sent_0*_is_*sent_1*.*sep+*" \
    --mapping "{'0':'great','1':'terrible'}" \
    --max_seq_length 128
