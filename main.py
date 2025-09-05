# main.py
import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="CSV Preview CLI")
    parser.add_argument("csv_path", help="Path to the CSV file")
    args = parser.parse_args()

    df = pd.read_csv(args.csv_path)
    print(df.head())

if __name__ == "__main__":
    main()