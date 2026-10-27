import pandas as pd

df = pd.read_csv('./week2/faqs.csv')

clean_df = df.copy()

clean_df["question"] = (
    clean_df["question"]
    .str.lower()                 
    .str.strip()                 
    .str.replace(r"[^\w\s]", "", regex=True)  
    .str.replace(r"\s+", " ", regex=True) 
)

clean_df["answer"] = (
    clean_df["answer"]
    .str.lower()
    .str.strip()
    .str.replace(r"[^\w\s]", "", regex=True)
    .str.replace(r"\s+", " ", regex=True)
)

print(clean_df)