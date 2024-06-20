# -*- coding: utf-8 -*-
"""sentiment_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15oZDtqOI0yVZoqhjO4HbrMt0W5x9MqM1
"""

# -*- coding: utf-8 -*-
"""
sentiment_analysis.py

Script to perform sentiment analysis on Turkish text data using pre-trained transformer models.
"""

import pandas as pd
import torch
import time
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from scipy.special import softmax

# Define models as a dictionary where keys are model names and values are model identifiers
models = {
    "peft_model": "VRLLab/TurkishBERTweet-Lora-SA",
    "emre_model": "emre/turkish-sentiment-analysis",
    "bounti_model": "akoksal/bounti",
    "xlm_model": "cardiffnlp/twitter-xlm-roberta-base-sentiment"
}

# Load datasets (ensure your dataset files are in the same directory)
data_df1 = pd.read_csv("data1.csv")
data_df2 = pd.read_csv("data2.csv")

# Combine or filter the DataFrame as needed
# For example, using data_df1 for further processing
df_filtered = data_df1  # Placeholder: adjust according to your actual logic

# Initialize lists to store results for each model
all_results = {model_name: [] for model_name in models}

# Load and analyze with each model
for model_name, model_id in models.items():
    print(f"Running sentiment analysis with {model_name}...")

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSequenceClassification.from_pretrained(model_id)

    # Prepare the text and labels
    text_list = df_filtered['Text'].tolist()
    labels_list = df_filtered['Label'].tolist()  # Assuming the column with original labels is called 'Label'

    result_list = []

    batch_size = 1

    # Perform sentiment analysis in batches
    for i in range(0, len(text_list), batch_size):
        batch = text_list[i:i + batch_size]
        labels_batch = labels_list[i:i + batch_size]
        start_time = time.time()

        encoded_inputs = tokenizer(
            batch,
            padding=True,
            truncation=True,
            return_tensors='pt',
            max_length=514  # Adjust max_length if needed
        )

        with torch.no_grad():
            outputs = model(**encoded_inputs)
            scores = softmax(outputs.logits.detach().numpy(), axis=1)
            predicted_labels = [model.config.id2label[score.argmax().item()] for score in scores]

            for text, score, predicted_label, label in zip(batch, scores, predicted_labels, labels_batch):
                result = {
                    "text": text,
                    "scores": score.tolist(),
                    "predicted_label": predicted_label,
                    "original_label": label,
                    "model_used": model_name  # Add the model name used for each result
                }
                result_list.append(result)

        end_time = time.time()
        batch_execution_time = end_time - start_time
        print(f"Batch {i}-{i+batch_size-1} Execution time: {batch_execution_time} seconds")

    all_results[model_name] = result_list

# Save the results to CSV files for each model
for model_name, results in all_results.items():
    result_df = pd.DataFrame(results)
    result_df.to_csv(f"{model_name}_results.csv", index=False)

