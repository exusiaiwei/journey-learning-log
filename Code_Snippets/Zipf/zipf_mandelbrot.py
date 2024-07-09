import numpy as np
import scipy.optimize as opt
from collections import Counter
import matplotlib.pyplot as plt
import jieba
import matplotlib.font_manager as fm

def preprocess_text(text):
    # 使用jieba进行中文分词
    words = jieba.lcut(text)
    # 去除空白字符
    words = [word for word in words if word.strip() != '']
    return words

def zipf_mandelbrot_pmf(x, a, b, n):
    F_n = sum((b + i) ** -a for i in range(1, n + 1))
    return (b + x) ** -a / F_n

def negative_log_likelihood(params, ranks, frequencies, n):
    a, b = params
    pmf_values = np.array([zipf_mandelbrot_pmf(rank, a, b, n) for rank in ranks])
    log_likelihood = -np.sum(frequencies * np.log(pmf_values))
    return log_likelihood

def fit_zipf_mandelbrot_distribution(words):
    word_counts = Counter(words)
    sorted_word_counts = sorted(word_counts.values(), reverse=True)
    ranks = np.arange(1, len(sorted_word_counts) + 1)
    frequencies = np.array(sorted_word_counts)
    n = len(sorted_word_counts)

    # 初始参数猜测
    initial_params = [1.0, 1.0]

    # 最小化负对数似然函数
    result = opt.minimize(negative_log_likelihood, initial_params, args=(ranks, frequencies, n), bounds=[(0, None), (0, None)])

    if result.success:
        fitted_params = result.x
    else:
        raise RuntimeError("优化失败")

    return ranks, sorted_word_counts, fitted_params

def plot_zipf_mandelbrot_fit(ranks, sorted_word_counts, params):
    a, b = params
    n = len(sorted_word_counts)
    pmf_values = np.array([zipf_mandelbrot_pmf(rank, a, b, n) for rank in ranks])
    fitted_frequencies = pmf_values * sum(sorted_word_counts)

    plt.figure(figsize=(10, 6))

    # 设置中文字体
    font_path = r'C:\Users\Star\AppData\Local\Microsoft\Windows\Fonts\LXGWBright-Regular.otf'  # 这里指定你系统中存在的中文字体路径
    prop = fm.FontProperties(fname=font_path)

    plt.plot(ranks, sorted_word_counts, 'o', label='实际数据')
    plt.plot(ranks, fitted_frequencies, 'r-', label='齐普夫-曼德博拟合')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('排名', fontsize=14, fontproperties=prop)
    plt.ylabel('频率', fontsize=14, fontproperties=prop)
    plt.legend(prop=prop)
    plt.title('齐普夫-曼德博分布拟合', fontsize=16, fontproperties=prop)

    # 添加必要的文字说明
    plt.text(1, max(sorted_word_counts), f"拟合参数: a = {a:.4f}, b = {b:.4f}", fontsize=12, fontproperties=prop, verticalalignment='top')

    plt.show()

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main(file_path):
    text = read_text_file(file_path)
    words = preprocess_text(text)
    ranks, sorted_word_counts, params = fit_zipf_mandelbrot_distribution(words)
    plot_zipf_mandelbrot_fit(ranks, sorted_word_counts, params)
    print("拟合参数: a =", params[0], ", b =", params[1])

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python zipf_mandelbrot.py <file_path>")
    else:
        file_path = sys.argv[1]
        main(file_path)
