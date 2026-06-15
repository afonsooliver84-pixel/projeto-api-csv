
from src.api import get_data
from src.process import save_to_csv, analyze_data
def main():
    data = get_data()
    save_to_csv(data)

    result = analyze_data()
    print("Top 5 criptomoedas por preço:")
    print(result)

if __name__ == "__main__":
    main()