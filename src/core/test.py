# Ganked from https://seaborn.pydata.org/examples/many_pairwise_correlations.html
# Assumes you have run `pip install numpy pandas matplotlib scikit-learn seaborn`

# Standard imports
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# For this example we'll use Seaborn, which has some nice built in plots
import seaborn as sns

# Grab a data set from scikit-learn
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()
df = pd.DataFrame(
    np.c_[data['data'], data['target']],
    columns=data['feature_names'] + ['target']
)

# Create the correlation matrix
corr = df.corr()

# Generate a mask for the upper triangle; True = do NOT show
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
# More details at https://seaborn.pydata.org/generated/seaborn.heatmap.html
sns.heatmap(
    corr,          # The data to plot
    mask=mask,     # Mask some cells
    cmap=cmap,     # What colors to plot the heatmap as
    annot=True,    # Should the values be plotted in the cells?
    vmax=.3,       # The maximum value of the legend. All higher vals will be same color
    vmin=-.3,      # The minimum value of the legend. All lower vals will be same color
    center=0,      # The center value of the legend. With divergent cmap, where white is
    square=True,   # Force cells to be square
    linewidths=.5, # Width of lines that divide cells
    cbar_kws={"shrink": .5}  # Extra kwargs for the legend; in this case, shrink by 50%
)

# You can save this as a png with
f.savefig('heatmap_colored_correlation_matrix_seaborn_python.png')
