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


def load_data(file_path):
    """
    Load a CSV file and return the DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {file_path} successfully.")
        return df
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None


def run_sentiment_analysis(model_name, model_id, df, batch_size=1):
    """
    Run sentiment analysis using a specified model on the provided DataFrame.
    """
    print(f"Running sentiment analysis with {model_name}...")

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSequenceClassification.from_pretrained(model_id)

    # Prepare the text and labels
    text_list = df['Text'].tolist()
    labels_list = df.get('Label', ['Unknown'] * len(text_list))  # Default to 'Unknown' if no Label column

    results = []

    # Perform sentiment analysis in batches
    for i in range(0, len(text_list), batch_size):
        batch = text_list[i:i + batch_size]
        labels_batch = labels_list[i:i + batch_size]
        start_time = time.time()

        # Tokenize and predict
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
            predicted_labels = [model.config.id2label[score.argmax()] for score in scores]

            # Store results
            for text, score, predicted_label, label in zip(batch, scores, predicted_labels, labels_batch):
                results.append({
                    "text": text,
                    "scores": score.tolist(),
                    "predicted_label": predicted_label,
                    "original_label": label,
                    "model_used": model_name
                })

        end_time = time.time()
        print(f"Batch {i}-{i+batch_size-1} Execution time: {end_time - start_time:.2f} seconds")

    return results


def main():
    """
    Main function to load data, run sentiment analysis, and save results.
    """
    # Load datasets
    data1 = load_data("data1.csv")
    data2 = load_data("data2.csv")

    if data1 is None or data2 is None:
        print("Error: Could not load datasets. Exiting...")
        return

    # Combine datasets if needed (placeholder logic)
    df_combined = pd.concat([data1, data2])

    all_results = {}

    # Run sentiment analysis for each model
    for model_name, model_id in models.items():
        results = run_sentiment_analysis(model_name, model_id, df_combined)
        all_results[model_name] = results

        # Save results to CSV
        result_df = pd.DataFrame(results)
        result_df.to_csv(f"{model_name}_results.csv", index=False)
        print(f"Results saved to {model_name}_results.csv")

    print("Sentiment analysis completed successfully.")


if __name__ == "__main__":
    main()
