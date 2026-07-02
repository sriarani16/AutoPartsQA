import pandas as pd
from rapidfuzz import fuzz, process

def ai_duplicate_detection(df):
    results = []

    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            name1 = df.iloc[i]["part_name"]
            name2 = df.iloc[j]["part_name"]

            score = fuzz.ratio(name1, name2)

            if score >= 85:  # similarity threshold
                results.append({
                    "part_id_1": df.iloc[i]["part_id"],
                    "part_id_2": df.iloc[j]["part_id"],
                    "name_1": name1,
                    "name_2": name2,
                    "similarity": score
                })

    return pd.DataFrame(results)
