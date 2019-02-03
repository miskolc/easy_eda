"""Module with class definitions for performing EDA."""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import seaborn as sns

def bar_plot(df, x, y, figsize=(20, 25), **kwargs):
    ax = df.plot.barh(
        x=x, y=y, figsize=figsize, **kwargs)
    ax.set_title(title + f" - Shape of Data {df.shape}")
    plt.show()

class NullsAnalyzer():
    """
    Analyzer of Null counts.

    >>> nulls_analyzer = NullsAnalyzer(df)
    >>> nulls_analyzer.plot(title="Example plot")
    """
    def __init__(self, df, null_value=None):
        self.df = df
        if null_value is None:
            self.nulls_df = pd.DataFrame(self.df.isnull().sum())
        else:
            self.nulls_df = pd.DataFrame(self.df.eq(null_value).sum())
        self.nulls_df["cols"] = self.nulls_df.index
        self.nulls_df["nulls"] = self.nulls_df[0]
        self.nulls_df.sort_values(by=['cols'], inplace=True)
    
    def plot(self, title="", **kwargs):
        bar_plot(self.nulls_df, x="cols", y="nulls")

    def summary(self):
        return self.nulls_df[["nulls"]]

class CategoricalAnalyzer():
    """
    Analyzer for Categorical Variables.
    
    >>> scatter_analyzer = CategoricalAnalyzer(df)
    >>> scatter_analyzer.plot("column1", "column2", title="Example plot")
    """
    def __init__(self, df):
        self.df = df

    def plot(
        self, x, y, title="", xlim=(-100, 100), vline=0, vlines=[],
        figsize=(20, 20), palette="Set3", inner="quartile", **kwargs):
        plt.figure(figsize=figsize)
        ax = sns.violinplot(
            x=x, y=y,
            data=self.df,
            palette=palette,
            inner=inner,
            **kwargs
        )
        ax.set_xlim(*xlim)
        plt.axvline(vline)
        for vline in vlines:
            plt.axvline(vline, color='r', linestyle='--')
        ax.set_title(title + f" - Shape of Data {self.df.shape}")
        plt.show()
        
class ScatterAnalyzer():
    """
    Analyzer for Numeric Variable non-monotonic correlations.
    
    >>> scatter_analyzer = ScatterAnalyzer(df)
    >>> scatter_analyzer.plot(title="Example plot")
    """
    def __init__(self, df):
        self.df = df

    def plot(self, alpha=0.2, figsize=(20, 20), **kwargs):
        scatter_matrix(
            self.df, alpha=alpha,# ax=ax,
            figsize=figsize, diagonal='kde'
        )
        plt.show()

class NumericAnalyzer():
    """
    Analyzer for Numeric Variable correlations.
    
    >>> numeric_analyzer = NumericAnalyzer(df)
    >>> numeric_analyzer.plot(title="Example plot")
    """
    def __init__(self, df):
        self.df = df
    
    def plot(self, method="pearson", title="", figsize=(20,20), cmap="YlGnBu", annot=True, **kwargs):
        corr_data = self.df.corr(method=method)
        plt.figure(figsize=figsize)
        ax = sns.heatmap(corr_data, center=0, cmap=cmap, annot=annot, **kwargs)
        ax.set_title(title + f" - Shape of Data {self.df.shape}")
        plt.show()