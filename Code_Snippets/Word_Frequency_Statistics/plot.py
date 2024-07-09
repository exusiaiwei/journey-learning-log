import plotly.express as px

def plot_word_frequency(word_counts):
    words, frequencies = zip(*word_counts.most_common(50))
    fig = px.line(x=range(len(words)), y=frequencies, text=words, labels={"x": "Word Rank", "y": "Frequency"})
    fig.update_traces(textposition='top center')
    fig.show()
