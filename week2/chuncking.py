from cleaning import clean_df

clean_df["text"] = (
    "Question: " + clean_df["question"]
    + " Answer: " + clean_df["answer"]
)

clean_df[["question", "answer", "text"]]

chunks = clean_df["text"].tolist()

chunk_ids = [f"faq_{i}" for i in range(len(chunks))]

for chunk_id, chunk in zip(chunk_ids, chunks):
    print(f"{chunk_id}: {chunk}\n")
