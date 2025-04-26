import pandas as pd
import json

# Load the data
with open("judge-gemini-with-metatuning-clever.json", "r") as f:
    judge_data_with_metatuning = json.load(f)

with open("judge-gemini-wo-metatuning-clever.json", "r") as f:
    judge_data_wo_metatuning = json.load(f)

# Initialize lists to store data
data = []

# Iterate through the data and collect information
for video_filename in judge_data_with_metatuning.keys():
    for question_idx in judge_data_with_metatuning[video_filename].keys():
        row = {
            "video_filename": video_filename,
            "question_idx": question_idx,
            "question": judge_data_with_metatuning[video_filename][question_idx]["question"],
            "question_type": judge_data_with_metatuning[video_filename][question_idx]["question_type"],
            "correct_answer": judge_data_with_metatuning[video_filename][question_idx]["answer"],
            "llm_answer_with_metatuning": judge_data_with_metatuning[video_filename][question_idx]["llm_answer"],
            "judge_answer_with_metatuning": judge_data_with_metatuning[video_filename][question_idx]["judge_answer"],
            "llm_answer_wo_metatuning": judge_data_wo_metatuning[video_filename][question_idx]["llm_answer"],
            "judge_answer_wo_metatuning": judge_data_wo_metatuning[video_filename][question_idx]["judge_answer"]
        }
        data.append(row)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("judge_results.csv", index=False)

print("DataFrame created and saved to judge_results.csv")
print("\nDataFrame shape:", df.shape)
print("\nFirst few rows:")
print(df.head()) 