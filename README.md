# Sentiment Analysis with Pre-trained Transformer Models and Turkish-SAD

This repository contains a Python script to perform sentiment analysis on Turkish text data using multiple pre-trained transformer models and list of Turkish Sentiment Analysis Datasets between 2012 to 2022.

## Requirements

- pandas
- torch
- transformers
- scipy

You can install the required packages using pip:

```bash
pip install pandas torch transformers scipy
Usage

Ensure you have the necessary datasets in the same directory as the script.
Adjust the script if needed to filter your DataFrame properly (df_filtered).
Run the script:
The script will output the sentiment analysis results to CSV files (peft_model_results.csv, emre_model_results.csv, bounti_model_results.csv, xlm_model_results.csv) for each model.

Pre-trained Models Used

peft_model: VRLLab/TurkishBERTweet-Lora-SA
emre_model: emre/turkish-sentiment-analysis
bounti_model: akoksal/bounti
xlm_model: cardiffnlp/twitter-xlm-roberta-base-sentiment
Using Google Colab

Enabling TPU and High RAM

To use this script on Google Colab with TPU and high RAM, follow these steps:

Open Google Colab: Go to Google Colab.

Upload the script: Upload sentiment_analysis.py and your datasets (data1.csv, data2.csv) to Colab.

Enable TPU:

Go to Runtime > Change runtime type.
Select TPU from the Hardware accelerator dropdown menu.
Enable High RAM:

Go to Runtime > Manage sessions.
Click on the current session.
Select High-RAM from the options available.
