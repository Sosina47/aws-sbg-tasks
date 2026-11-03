# Breaking the Spam Filter

## 1. Project Overview

This project explores how a basic machine learning spam filter can be fooled by slightly changing the wording of SMS messages.

The classifier uses **TF-IDF** to convert text into numerical features and **Multinomial Naive Bayes** to classify messages as either:

- `spam` — unwanted or suspicious messages.
- `ham` — legitimate messages.

The goal is not just to build a spam detector, but to investigate its weaknesses through adversarial testing.

## 2. How It Works

The spam detection process has five main steps.

### Step 1: Prepare the Dataset

We created a small SMS dataset containing spam and legitimate messages. Each message has a corresponding label.

The labels and messages must remain aligned: each message's label describes that exact message.

> Note: This is a small demonstration dataset, not the full SMS Spam Collection dataset. Its results are useful for illustrating concepts, not measuring real-world performance.

### Step 2: Split the Dataset

We divide the data into training and testing sets:

```python
X_train, X_test, y_train, y_test = train_test_split(
    emails,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)
```

- 80% of the messages are used for training.
- 20% are reserved for testing.
- `stratify=labels` preserves the class proportions in both sets.
- `random_state=42` makes the split reproducible.

### Step 3: Convert Text into Numerical Features

Machine learning models need numerical input rather than raw text. We use TF-IDF (Term Frequency–Inverse Document Frequency) to represent each message as a numerical vector.

```python
vec = TfidfVectorizer()
X_train_features = vec.fit_transform(X_train)
```

TF-IDF gives words weights based on how frequently they appear in a message and how common they are across the training dataset.

We then use the fitted vectorizer to transform the test messages:

```python
X_test_features = vec.transform(X_test)
```

We use `transform()` rather than `fit_transform()` on test data so that the vectorizer does not learn from information it should not have seen during training.

### Step 4: Train the Classifier

We use Multinomial Naive Bayes:

```python
model = MultinomialNB()
model.fit(X_train_features, y_train)
```

The model learns statistical relationships between words and the spam/ham labels.

For example, if words such as `prize`, `claim`, and `reward` frequently appear in spam messages in the training data, the model may learn that those words provide evidence for the spam class.

It does not understand the actual meaning of a sentence. It makes predictions using learned probabilities.

### Step 5: Make Predictions

For new messages, we first convert them using the same fitted TF-IDF vectorizer, then ask the trained model to predict their labels:

```python
new_features = vec.transform(new_messages)
predictions = model.predict(new_features)
```

The model returns either `spam` or `ham` for each message.

## 3. Adversarial Testing

We tested the classifier against three types of messages designed to expose weaknesses.

### Attack 1: Obfuscation

We changed ordinary characters into numbers to hide recognizable words.

Example:

- Original: `Congratulations! You won a free prize!`
- Modified: `C0ngratulati0ns! Y0u w0n a fr33 pr1ze!`

**Observed result:**

| Measurement | Result |
|---|---:|
| Original prediction | spam |
| Obfuscated prediction | ham |
| Original non-zero TF-IDF features | 5 |
| Obfuscated non-zero TF-IDF features | 0 |

**Analysis:** The modified message was classified as ham because none of its tokens matched the vectorizer's learned vocabulary. The model received an all-zero feature vector and lost the evidence it normally uses to identify spam.

### Attack 2: Negation

We tested whether adding negative wording changes the classification.

Examples:

- `You have won a free prize!`
- `You have NOT won a free prize!`
- `You have not won anything. This is a scam warning.`

**What this tests:** The model may focus on words such as `won`, `free`, and `prize` without understanding that adding `not` reverses the meaning.

### Attack 3: Business and Polite Language

We tested legitimate-sounding messages that contain words commonly associated with spam.

Examples:

- `Your free prize claim has been received by our office.`
- `Please review our special offer before tomorrow.`
- `Thank you for contacting our customer service team.`
- `We received your request and will contact you tomorrow.`

**What this tests:** The model may classify a legitimate message as spam simply because it contains words that were strongly associated with spam in its training data.

## 4. Results Table

| Test | Weakness investigated | Result / observation |
|---|---|---|
| Obfuscation | Vocabulary mismatch | Original predicted spam; modified message predicted ham. Its TF-IDF vector contained zero non-zero features. |
| Negation | Lack of contextual understanding | Tested whether negative wording changes the prediction. |
| Business language | Over-reliance on spam-associated words | Tested whether legitimate business messages trigger spam predictions. |

*The negation and business-language predictions should be filled in using the actual outputs from your notebook.*

## 5. Possible Improvements

| Weakness | Possible improvement |
|---|---|
| Obfuscation | Normalize modified text and use character-level TF-IDF features. |
| Negation | Include more examples with positive and negative meanings; consider context-aware language models. |
| Business-language false positives | Train with a larger, more diverse dataset containing legitimate business messages. |

## 6. Conclusion

This experiment demonstrates that a basic spam classifier can perform well on familiar patterns while remaining vulnerable to small changes in wording.

The obfuscation experiment showed a clear failure: changing letters into numbers caused the message to produce an all-zero TF-IDF vector, leading to a ham prediction.

The negation and business-language tests investigate two additional limitations: the model's inability to reliably understand sentence context and its dependence on statistical word associations.

The main lesson is that **recognizing familiar words is not the same as understanding language**. A more robust spam detector needs diverse training data, better text processing, and potentially models that can capture context.
