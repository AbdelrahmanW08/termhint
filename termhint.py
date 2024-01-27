import tensorflow as tf
import pandas as pd
from tensorflow.keras import layers
from tensorflow.keras.layers import TextVectorization
import tensorflow_hub as hub

df = pd.read_csv('dataset.csv')
df = df.dropna()
df = df.sample(frac=1, ignore_index=True)

text_vectorizer = TextVectorization(max_tokens=12690,
                                    output_sequence_length=1)

text_vectorizer.adapt(df['Word'])
tokenized_words = tf.squeeze(text_vectorizer(df['Word']))
tokenized_words_one_hot = tf.squeeze(tf.one_hot(tokenized_words,axis=1,depth=num_words))

tf_hub_embedding_layer = hub.KerasLayer('https://tfhub.dev/google/universal-sentence-encoder/4',
                                        trainable=False,
                                        name='universal_sentence_encoder')

inputs = layers.Input(shape=[], dtype=tf.string)
use_embedding = tf_hub_embedding_layer(inputs)
x = layers.Dense(128, activation ='relu')(use_embedding)
outputs = layers.Dense(len(text_vectorizer.get_vocabulary()), activation ='softmax')(x)
model = tf.keras.Model(inputs, outputs)

model.compile(loss='categorical_crossentropy',
                optimizer=tf.keras.optimizers.Adam(),
                metrics=['accuracy'])

model.fit(df['Meaning'], tokenized_words_one_hot,
          batch_size=128,
          epochs=15)