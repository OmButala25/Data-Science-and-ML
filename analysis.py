import pandas as pd
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
import syllables

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to calculate text analysis variables
def calculate_text_analysis(text):
    # Cleaning using Stop Words Lists
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in word_tokenize(text) if word.isalpha() and word.lower() not in stop_words]

    # Analysis of Readability
    sentences = sent_tokenize(text)
    avg_sentence_length = len(words) / len(sentences)
    complex_words = [word for word in words if syllables.estimate(word) > 2]
    percentage_complex_words = (len(complex_words) / len(words)) * 100
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

    # Average Number of Words Per Sentence
    avg_words_per_sentence = len(words) / len(sentences)

    # Complex Word Count
    complex_word_count = len(complex_words)

    # Word Count
    word_count = len(words)

    # Syllable Count Per Word
    syllable_per_word = sum(syllables.estimate(word) for word in words) / len(words)

    # Sentiment Analysis using TextBlob
    blob = TextBlob(text)
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity

    # Personal Pronouns
    personal_pronouns = len(re.findall(r'\b(?:i|we|my|ours|us)\b', text, flags=re.IGNORECASE))

    # Average Word Length
    avg_word_length = sum(len(word) for word in words) / len(words)

    return [
        polarity_score,
        -polarity_score,
        polarity_score,
        subjectivity_score,
        avg_sentence_length,
        percentage_complex_words,
        fog_index,
        avg_words_per_sentence,
        complex_word_count,
        word_count,
        syllable_per_word,
        personal_pronouns,
        avg_word_length
    ]

# Read the output structure Excel file
output_structure_file_path = 'Output Data Structure.xlsx'
output_df = pd.read_excel(output_structure_file_path)

# Iterate through each row in the output DataFrame
for index, row in output_df.iterrows():
    url_id = row['URL_ID']

    # Read the extracted text from the corresponding text file
    text_file_path = f'{url_id}.txt'
    with open(text_file_path, 'r', encoding='utf-8') as file:
        extracted_text = file.read()

    # Calculate text analysis variables
    analysis_results = calculate_text_analysis(extracted_text)

    # Update the output DataFrame with the computed values
    output_df.iloc[index, 2:] = analysis_results

# Save the updated output DataFrame to a new Excel file
output_df.to_excel('TextAnalysisOutput.xlsx', index=False)
print("Textual analysis complete.")
