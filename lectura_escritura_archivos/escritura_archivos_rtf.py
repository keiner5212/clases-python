import pandas as pd

# Create a Pandas DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
})

# Convert the DataFrame to an RTF table
rtf_table = "{\\rtf1\\ansi\\deff0{\\fonttbl{\\f0 Arial;}}{\\colortbl;\\red0\\green0\\blue0;}\\pard\\plain\\f0\\fs20 "
for _, row in df.iterrows():
    rtf_table += "\\cf0 " + " & ".join(map(str, row)) + " \\\\ \\par "
rtf_table += "}"

# Write the RTF table to a file
with open("./recursos/output.rtf", "w") as f:
    f.write(rtf_table)
