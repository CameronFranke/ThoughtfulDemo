# ThoughtfulDemo

### Explanation ###

This approach uses a sentence embedding to map a user query to the most similar question listed in the qanda file. If a similar question is found above the specified threshold then that answer is provided. If not an error
response is returned. To ensure robustness I created 3 alternate promps and used them to make sure matches were found with reasonable accuracy and that the mapping from new user prompt to canned Q&A response is made. I also used the alternate responsed to find the minimim similarity threshold that can be considered to constitute a good question to question mapping.


### Setup ###

python -m venv camDemo

source camDemo/bin/activate

pip install sentence_transformers

git clone git@github.com:CameronFranke/ThoughtfulDemo.git

cd ThoughtfulDemo

python explore_thresholds.py (optional)
python agent.py



### EXPLORATION OF THRESHOLDS: ###

## Exploring mappings for original question: 'What does the eligibility verification agent (EVA) do?' ##
- Alternate phrasing: 'Can you explain what EVA is used for?'
  -> Mapped to: 'What does the eligibility verification agent (EVA) do?' (Similarity: 0.5185)
  -> Correct mapping? Yes

- Alternate phrasing: 'What is the role of the eligibility verification agent?'
  -> Mapped to: 'What does the eligibility verification agent (EVA) do?' (Similarity: 0.8690)
  -> Correct mapping? Yes

- Alternate phrasing: 'Tell me about the function of the EVA agent.'
  -> Mapped to: 'What does the eligibility verification agent (EVA) do?' (Similarity: 0.6338)
  -> Correct mapping? Yes


## Exploring mappings for original question: 'What does the claims processing agent (CAM) do?' ##
- Alternate phrasing: 'How does the claims processing agent help?'
  -> Mapped to: 'What does the claims processing agent (CAM) do?' (Similarity: 0.8223)
  -> Correct mapping? Yes

- Alternate phrasing: 'What’s the purpose of the CAM agent?'
  -> Mapped to: 'What does the claims processing agent (CAM) do?' (Similarity: 0.6824)
  -> Correct mapping? Yes

- Alternate phrasing: 'Describe what the CAM agent is responsible for.'
  -> Mapped to: 'What does the claims processing agent (CAM) do?' (Similarity: 0.7137)
  -> Correct mapping? Yes


## Exploring mappings for original question: 'How does the payment posting agent (PHIL) work?' ##
- Alternate phrasing: 'What’s the role of PHIL in payment posting?'
  -> Mapped to: 'How does the payment posting agent (PHIL) work?' (Similarity: 0.8450)
  -> Correct mapping? Yes

- Alternate phrasing: 'Can you tell me how PHIL functions?'
  -> Mapped to: 'How does the payment posting agent (PHIL) work?' (Similarity: 0.4034) <----
  -> Correct mapping? Yes

- Alternate phrasing: 'Explain the purpose of the payment posting agent.'
  -> Mapped to: 'How does the payment posting agent (PHIL) work?' (Similarity: 0.8774)
  -> Correct mapping? Yes


## Exploring mappings for original question: 'Tell me about Thoughtful AI's Agents.' ##
- Alternate phrasing: 'Give me an overview of Thoughtful AI’s agents.'
  -> Mapped to: 'Tell me about Thoughtful AI's Agents.' (Similarity: 0.9573)
  -> Correct mapping? Yes

- Alternate phrasing: 'What kind of agents does Thoughtful AI offer?'
  -> Mapped to: 'Tell me about Thoughtful AI's Agents.' (Similarity: 0.9349)
  -> Correct mapping? Yes

- Alternate phrasing: 'Tell me more about the AI agents provided by Thoughtful.'
  -> Mapped to: 'Tell me about Thoughtful AI's Agents.' (Similarity: 0.9557)
  -> Correct mapping? Yes


## Exploring mappings for original question: 'What are the benefits of using Thoughtful AI's agents?' ##
- Alternate phrasing: 'How does using Thoughtful AI agents help?'
  -> Mapped to: 'What are the benefits of using Thoughtful AI's agents?' (Similarity: 0.9334)
  -> Correct mapping? Yes

- Alternate phrasing: 'What are the advantages of Thoughtful AI's automation agents?'
  -> Mapped to: 'What are the benefits of using Thoughtful AI's agents?' (Similarity: 0.8719)
  -> Correct mapping? Yes

- Alternate phrasing: 'Can you list the benefits of Thoughtful's agents?'
  -> Mapped to: 'What are the benefits of using Thoughtful AI's agents?' (Similarity: 0.7864)
  -> Correct mapping? Yes

## Summary ##
Total Alternate Phrasings: 15
Correct Mappings: 15
Accuracy: 100.00%

We can choose a threshold of 0.4

### Example ###
(camDemo) /Users/cam/ThoughtfulDemo [main]% python agent.py
Chatbot is ready. You can start asking questions! Type 'exit' to quit.
User: What is EVA used for?
Agent: EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.