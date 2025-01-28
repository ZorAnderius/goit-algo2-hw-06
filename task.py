import requests
from collections import Counter
from matplotlib import pyplot as plt

from map_reduce import map_reduce

def get_text(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return None

def visualize_top_words(res: dict) -> None:
    try:
        top_10 = Counter(res).most_common(10)
        labels, values = zip(*top_10)
        plt.figure(figsize=(10, 5))
        plt.barh(labels, values, color=["#99CCFF"])
        plt.xlabel("Quantity")
        plt.ylabel("Word")
        plt.title("Top10 most frequent words")

        plt.gca().invert_yaxis()
        plt.show()
    except Exception as e:
        print('Plotting error:', e)

if __name__ == '__main__':
    url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    text = get_text(url)
    if text:
        res = map_reduce(get_text(url))
        visualize_top_words(res)
    else:
        print('Text not found')
