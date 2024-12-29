import json

examples_file = "nsynth/data/nsynth-train/examples.json"

# Load json file
with open(examples_file, "r") as file:
    examples = json.load(file)

# Filter out entries whose keys do not contain "keyboard"
filtered_examples = {key: value for key, value in examples.items() if "keyboard" in key}

# Save the filtered examples back to the examples.json file
with open(examples_file, "w") as file:
    json.dump(filtered_examples, file, indent=4)

print(f"Filtered {len(examples) - len(filtered_examples)} entries without 'keyboard' in their name.")