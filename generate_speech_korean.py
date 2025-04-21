import pandas as pd
import os
import re
from gtts import gTTS
import time

# Sanitize filenames
def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

output_dir = "korean_audio"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

df = pd.read_csv("korean_vocab3.csv", encoding="utf-8")
df.columns = df.columns.str.strip()

for index, row in df.iterrows():
    try:
        subcategory = sanitize_filename(row['하위 카테고리'].strip())
        word = sanitize_filename(row['단어'].strip())
        example = row['예문'].strip()
        word_filename = f"{output_dir}/{subcategory}-{word}.mp3"
        example_filename = f"{output_dir}/{subcategory}-{word}-example-sentence.mp3"
        
        # Generate word audio
        print(f"Generating audio for word: {row['단어']}")
        word_tts = gTTS(row['단어'], lang='ko')
        word_tts.save(word_filename)
        
        # Generate example sentence audio
        print(f"Generating audio for example: {example}")
        example_tts = gTTS(example, lang='ko')
        example_tts.save(example_filename)
        
        # Add delay to avoid hitting Google's rate limits
        time.sleep(1)
        print(f"Processed {index+1}/{len(df)} entries.")
        
    except Exception as e:
        print(f"Error processing entry {index+1}: {str(e)}")
        print(f"Skipping to next entry...")
        continue

print("Audio generation complete!")