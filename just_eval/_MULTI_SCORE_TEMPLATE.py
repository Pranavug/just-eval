MULTI_SCORE_TEMPLATE = """\
Please act as an impartial judge and evaluate the quality of the responses provided as compared to the provided ground truth. You will rate the quality of the output on multiple aspects such as Helpfulness, Clarity, Factuality, Depth, and Engagement.

## Query: 
${instruction}

## Ground Truth:
${ground_truth}
 
## Output:
${candidate}


## Evaluate

### Aspects 

- Helpfulness: Rate the response based on how well it addresses the user's query and provides a solution relevant to the ground truth. A score of 5 indicates the answer fully aids the user, while a 1 suggests it offers little to no help.

- Clarity: Rate the response based on how well-structured it is, with ideas presented in a clear and coherent manner. A high score of 5 means the answer is clear and logically structured, while a 1 suggests a disjointed or confusing reply.  

- Factuality: Evaluate the factual accuracy and truthfulness of the information provided as compared to the provided ground truth. A perfect 5 indicates the information is entirely correct and accurate, while a 1 suggests it has significant factual errors.

- Depth: Determine the level of detail and thoroughness in the response as compared to the provided ground truth. A score of 5 means the answer delves deeply into the topic, while a 1 indicates it barely scratches the surface.

- Engagement: Assess how engaging and natural the response sounds in a conversational context. A high score of 5 reflects a response that feels engaging and human-like in its tone, while a 1 indicates a robotic or boring reply.

### Format 

Given the query, please rate the quality of the output by scoring it from 1 to 5 individually on **each aspect**. 

- 1: strongly disagree 
- 2: disagree 
- 3: neutral
- 4: agree
- 5: strongly agree

Now, please output your scores and a short rationale below in a json format by filling in the placeholders in []:
```
{
    "helpfulness": {
        "reason": "[your rationale]",
        "score": "[score from 1 to 5]"
    },
    "clarity": {
        "reason": "[your rationale]",
        "score": "[score from 1 to 5]"
    },
    "factuality": {
        "reason": "[your rationale]",
        "score": "[score from 1 to 5]"
    },
    "depth": {
        "reason": "[your rationale]",
        "score": "[score from 1 to 5]"
    },
    "engagement": {
        "reason": "[your rationale]",
        "score": "[score from 1 to 5]"
    }
}
```
"""