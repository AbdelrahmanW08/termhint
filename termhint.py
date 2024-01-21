import tensorflow as tf
import pandas as pd
from tensorflow.keras.layers import TextVectorization

df = pd.read_csv('dataset.csv')
df = df.dropna()
df = df.sample(frac=1, ignore_index=True)

text_vectorizer = TextVectorization(max_tokens=12690,
                                    output_sequence_length=1)

text_vectorizer.adapt(df['Word'])
tokenized_words = tf.squeeze(text_vectorizer(df['Word']))
model = tf.keras.models.load_model('model')