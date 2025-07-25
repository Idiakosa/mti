import pandas as pd
import matplotlib.pyplot as plt

# Loading Data
data = pd.read_csv(r"C:\Users\kosa3\mti\toxicity_analysis\toxicophore_merged.csv")

# Filter for compounds/molecules with 0 to 2 toxicophores
filtered = data[(data['Toxicophore'] >= 0) & (data['Toxicophore'] <= 2)]

# Save the filtered data
filtered.to_csv("Filtered_Toxicity.csv", index=False)

# Check if any molecules passed
if filtered.empty:
    print("No molecules passed the toxicophore filter (0–2).")
else:
    print(f"{len(filtered)} molecules passed the toxicophore filter.")
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.bar(filtered.index, filtered['Toxicophore'], color='red')
    plt.xlabel("Molecule(Row Index)")
    plt.ylabel("# of Toxicophores")
    plt.title("Molecules with Toxicophores Between 0 and 2")
    plt.yticks([0, 1, 2])

    # Add value labels on top of each bar
    for i, val in enumerate(filtered['Toxicophore']):
        plt.text(filtered.index[i], val + 0.1, str(val), ha='center', va='bottom', fontsize=8)

    # Save the plot as a PNG
    plt.tight_layout()
    plt.savefig("Toxicophore_Plot.png")
    plt.close()

    print("Filtered data saved to 'Filtered_Toxicity.csv'")
    print("Plot saved as 'Toxicophore_Plot.png'")