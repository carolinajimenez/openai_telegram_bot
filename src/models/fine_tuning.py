# Standard library imports.
import os
import time
import requests

# Third party imports.
import openai
from openai import OpenAI


class OpenAITrainer:
    def __init__(self, data_train_path, data_val_path) -> None:
        self.data_train_path = data_train_path
        self.data_val_path = data_val_path

        OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def load_dataset(self):
        self.client.files.create(
            file=open(self.data_train_path, "rb"),
            purpose="fine-tune"
        )
        self.client.files.create(
            file=open(self.data_val_path, "rb"),
            purpose="fine-tune"
        )

    def fine_tune_model(self):
        self.client.fine_tuning.jobs.create(
            training_file="INGRESA EL FILE ID DEL ARCHIVO DE TRAIN", 
            validation_file='INGRESA EL FILE ID DEL ARCHIVO DE VAL',
            model="gpt-3.5-turbo-1106"
        )


def main():
    trainer = OpenAITrainer(
        "data/data_train.jsonl",
        "data/data_val.jsonl",
    )
    trainer.load_dataset()
    trainer.fine_tune_model()


if __name__ == "__main__":
    main()