import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class exploration:
    ###############################################################################
    # Visualization graphs
    ################################################################################

    def plot_heatmap(df: pd.DataFrame, title: str, cbar=False) -> None:
        ''' 
        heatmap: Plot rectangular data as a color-encoded matrix.
        heatmap of the dataframe
        cbar: Whether to draw a colorbar.
        title: Title of the plot
        df: dataframe to be plotted
        '''

        plt.figure(figsize=(13, 8))
        sns.heatmap(df, annot=True, cmap='viridis', vmin=0,
                    vmax=1, fmt='.2f', linewidths=.7, cbar=cbar)
        plt.title(title, size=20, fontweight='bold')
        plt.show()