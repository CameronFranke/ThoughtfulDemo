import json
from sentence_transformers import SentenceTransformer, util

# Load the model
MODEL = SentenceTransformer('all-MiniLM-L6-v2')
THRESHOLD = 0.4 # found with the explore_thresholds.py script

def load_qanda(file_name='qanda.json'):
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
        # Extract the 'questions' list from the JSON structure
        if 'questions' in data and isinstance(data['questions'], list):
            return data['questions']
        else:
            raise ValueError("The JSON structure is invalid. Expected a top-level 'questions' key containing a list of Q&A pairs.")
    except Exception as e:
        print(f"Error loading the Q&A file: {e}")
        return []

def get_response(user_input, qa_pairs, predefined_embeddings, debug=False):
    # Encode the user input
    user_embedding = MODEL.encode(user_input)

    # Compute cosine similarities
    similarities = util.cos_sim(user_embedding, predefined_embeddings)

    if debug:
        print("Similarity Scores:", similarities)

    # Find the best match
    best_match_idx = similarities.argmax()
    best_score = similarities[0][best_match_idx]

    # Set a threshold
    if best_score >= THRESHOLD:
        return qa_pairs[best_match_idx]['answer']
    else:
        return "I'm sorry, I don't have the information on that. How else can I assist you?"

def main(file_name='qanda.json', debug=False):
    # Load the Q&A pairs and encode the questions
    qa_pairs = load_qanda(file_name)
    if not qa_pairs:
        print("No valid Q&A pairs found. Exiting...")
        return

    predefined_embeddings = MODEL.encode([pair['question'] for pair in qa_pairs])

    print("Chatbot is ready. You can start asking questions! Type 'exit' to quit.")
    while True:
        user_input = input("User: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_response(user_input, qa_pairs, predefined_embeddings, debug)
        print(f"Agent: {response}")

# Example usage
if __name__ == "__main__":
    # Start the chat with 'qanda.json' file and enable debug mode if needed
    main(file_name='qanda.json', debug=False)
