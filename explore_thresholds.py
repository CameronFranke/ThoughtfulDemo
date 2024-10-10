import json
from sentence_transformers import SentenceTransformer, util

# Load the model
MODEL = SentenceTransformer('all-MiniLM-L6-v2')

# Load original Q&A pairs
def load_qanda(file_name='qanda.json'):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data['questions']

# Load alternate phrasing file
def load_alternates(file_name='alternate_qanda.json'):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data['alternates']

def explore_mappings(qa_file='qanda.json', alt_file='alternate_qanda.json'):
    # Load data from both files
    original_qas = load_qanda(qa_file)
    alternate_qas = load_alternates(alt_file)

    # Extract original questions
    original_questions = [pair['question'] for pair in original_qas]
    original_embeddings = MODEL.encode(original_questions)

    # To track mapping results
    total_phrasings = 0
    correct_mappings = 0

    # Iterate through each original question and its alternate phrasings
    for item in alternate_qas:
        original_question = item['original_question']
        original_index = original_questions.index(original_question)

        print(f"\n### Exploring mappings for original question: '{original_question}' ###")

        for alt in item['phrases']:
            # Encode the alternate phrasing
            alt_embedding = MODEL.encode(alt)

            # Compute similarity scores with all original questions
            similarities = util.cos_sim(alt_embedding, original_embeddings)[0]

            # Determine the index of the most similar original question
            best_match_idx = similarities.argmax().item()
            best_match_question = original_questions[best_match_idx]

            # Check if the most similar question matches the expected original question
            is_correct = (best_match_idx == original_index)

            # Update counters
            total_phrasings += 1
            correct_mappings += 1 if is_correct else 0

            # Display results for this alternate phrasing
            print(f"- Alternate phrasing: '{alt}'")
            print(f"  -> Mapped to: '{best_match_question}' (Similarity: {similarities[best_match_idx]:.4f})")
            print(f"  -> Correct mapping? {'Yes' if is_correct else 'No'}\n")

    # Display final summary
    accuracy = (correct_mappings / total_phrasings) * 100
    print(f"### Summary ###\nTotal Alternate Phrasings: {total_phrasings}\nCorrect Mappings: {correct_mappings}")
    print(f"Accuracy: {accuracy:.2f}%")

# Run the exploration
if __name__ == "__main__":
    explore_mappings(qa_file='qanda.json', alt_file='alternate_qanda.json')
