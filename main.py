# Import all the python package
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Convert star rating to sentiments
def startosentiment(_star):
    if _star >= 4:
        return 'pos'
    elif _star <= 2:
        return 'neg'
    else:
        return 'neu'

# Use Vader to analyse the sentences and convert the compound score to sentiments
def get_score(analyser, _text):
    vpolarity = analyser.polarity_scores(_text)
    # return vpolarity['compound']
    if vpolarity['compound'] > 0.05:
        return 'pos'
    elif vpolarity['compound'] < -0.05:
        return 'neg'
    else:
        return 'neu'

# Initilize the Vader Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Load the dataset into pandas dataframe
icreviews = pd.read_csv('reviews.csv')

# Data cleaning - fill 'title' column with blank if it is N/A
icreviews['title'] = icreviews['title'].fillna('')

# Combine title and text to a new column
icreviews['com_titletext'] = icreviews['title'] + " " + icreviews['text']

# Convert start rating to sentiments
icreviews['b_star'] = icreviews.apply(lambda x: startosentiment(x['stars']),axis=1)  

# Perform prediction on newly combined column 'title'+'text' and store the sentiments into new column
icreviews['com_score'] = icreviews.apply(lambda x: get_score(sia, x['com_titletext']),axis=1)

# Compute the confusion matrix
conf1 = metrics.confusion_matrix(icreviews['b_star'], icreviews['com_score'])

# Print the precision and recall, among other metrics
print(metrics.classification_report(icreviews['b_star'], icreviews['com_score'], digits=3))

# Plot the confusion matrix
group_counts = ["{0:0.0f}".format(value) for value in conf1.flatten()]
group_percentages = ["{0:.2%}".format(value) for value in conf1.flatten()/np.sum(conf1)]
labels = [f"{v2}\n{v3}" for v2, v3 in zip(group_counts,group_percentages)]
labels = np.asarray(labels).reshape(3,3)
x_axis_labels = ['neg','neu','pos'] # labels for x-axis
y_axis_labels = ['neg','neu','pos'] # labels for y-axis
sns.heatmap(conf1, xticklabels=x_axis_labels, yticklabels=y_axis_labels, annot=labels, fmt='', cmap="Blues").set_title("Ben & Jerry's")

# Overview of predicted sentiments by Vader
ax = sns.countplot(x ='com_score', data = icreviews)
ax.set(ylabel='Sentiment count', xlabel='Sentiments')
plt.show()

# Sentiment distribution pie plot
icreviews['com_score'].value_counts().plot.pie(autopct='%1.0f%%')
plt.title("Sentiment distribution pie chart")

# Top 10 ice cream brand sort by number of reviews
df_prod_reviewcount = icreviews['key'].value_counts().head(10).reset_index()
df_prod_isin = icreviews.loc[icreviews['key'].isin(df_prod_reviewcount['index'])]
ax1 = sns.countplot(x ='key', hue='com_score', data = df_prod_isin, order = df_prod_isin['key'].value_counts().index)
ax1.set(ylabel='Sentiment count', xlabel='Ice cream brand')

# Top 10 ice cream brand sort by positive review
df_posreview = icreviews.loc[icreviews['com_score'] == 'pos']
df_prod_positivecount = df_posreview['key'].value_counts().head(10).reset_index()
ax2 = sns.barplot(x ='index', y= 'key', data = df_prod_positivecount)
ax2.set(ylabel='Sentiment count', xlabel='Ice cream brand')

# Top 10 ice cream brand sort by negative review
dfnegreview = icreviews.loc[icreviews['com_score'] == 'neg']
df_prod_negcount = dfnegreview['key'].value_counts().head(10).reset_index()
ax2 = sns.barplot(x ='index', y= 'key', data = df_prod_negcount)
ax2.set(ylabel='Sentiment count', xlabel='Ice cream brand')

# Top 10 ice cream brand sort by neutral review
dfneureview = icreviews.loc[icreviews['com_score'] == 'neu']
df_prod_neucount = dfneureview['key'].value_counts().head(10).reset_index()
ax2 = sns.barplot(x ='index', y= 'key', data = df_prod_neucount)
ax2.set(ylabel='Sentiment count', xlabel='Ice cream brand')

# Top 10 ice cream brand sort by 4 or 5 stars rating
df_posreview = icreviews.loc[icreviews['b_star'] == 'pos']
df_prod_positivecount = df_posreview['key'].value_counts().head(10).reset_index()
ax2 = sns.barplot(x ='index', y= 'key', data = df_prod_positivecount)
ax2.set(ylabel='Sentiment count', xlabel='Ice cream brand')

# Top 10 ice cream brand sort by 1 or 2 stars rating
dfnegreview = icreviews.loc[icreviews['b_star'] == 'neg']
df_prod_negcount = dfnegreview['key'].value_counts().head(10).reset_index()
ax2 = sns.barplot(x ='index', y= 'key', data = df_prod_negcount)
ax2.set(ylabel='Sentiment count', xlabel='Ice cream brand')

# Top 10 ice cream brand sort by 3 stars rating
dfneureview = icreviews.loc[icreviews['b_star'] == 'neu']
df_prod_neucount = dfneureview['key'].value_counts().head(10).reset_index()
ax2 = sns.barplot(x ='index', y= 'key', data = df_prod_neucount)
ax2.set(ylabel='Sentiment count', xlabel='Ice cream brand')
