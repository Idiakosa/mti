import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV
df = pd.read_csv(r"C:\Users\kosa3\mti\physiochemical_analysis\Physiochemical.csv")

# Columns to use and convert to numeric (force errors to NaN)
expected_cols = ['nHA', 'nHD', 'nHet', 'Fsp3', 'logS', 'logD', 'logP', 'nStereo']

# Convert these columns to numeric, coercing errors to NaN
for col in expected_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with any NaN in those key columns
df = df.dropna(subset=expected_cols)

# Now apply filter criteria safely
filtered = df[
    (df['nHD'] >= 0) & (df['nHD'] <= 7) &
    (df['nHA'] >= 0) & (df['nHA'] <= 12) &
    (df['nStereo'] < 2) &
    (df['logP'] >= 0) & (df['logP'] <= 3) &
    (df['logD'] >= 1) & (df['logD'] <= 3) &
    (df['logS'] >= -4) & (df['logS'] <= 0.5) &
    (df['Fsp3'] > 0.41) &
    (df['nHet'] >= 1) & (df['nHet'] <= 15)
]

filtered.to_csv("Filtered_Physiochemical.csv", index=False)
print(f"Filtering complete. {len(filtered)} molecules passed the criteria.")

# Radar plot setup
categories = ['nHA', 'nHD', 'nHet', 'Fsp3', 'logS', 'logD', 'logP', 'nStereo']
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
ax.set_facecolor('lightgray')
plt.xticks(angles[:-1], categories, color='black', size=8)
ax.set_rlabel_position(30)
plt.yticks([1, 3, 5, 7], ["1", "3", "5", "7"], color="grey", size=7)
plt.ylim(0, 8)

# Plot up to 10 molecules
for i in range(min(10, len(filtered))):
    values = filtered.iloc[i][categories].tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=f"Molecule {i+1}")
    ax.fill(angles, values, alpha=0.1)

plt.subplots_adjust(right=0.75)
ax.legend(loc='center left', bbox_to_anchor=(1.2, 0.5), fontsize='small', ncol=1)

plt.savefig("physiochemical.png", bbox_inches='tight')
plt.show()
