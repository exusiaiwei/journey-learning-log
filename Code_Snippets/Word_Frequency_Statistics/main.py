from word_counter import count_words_in_files
from plot import plot_word_frequency

if __name__ == "__main__":
    directory = './data'
    word_counts = count_words_in_files(directory)
    plot_word_frequency(word_counts)
