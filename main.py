from processor import read_file, clean_data, insert_into_mongo
from validator import validate_data
from mongo_connection import get_collection

INPUT_FILE = "raw_data.csv"

def main():
    df = read_file(INPUT_FILE)
    df = clean_data(df)

    errors = validate_data(df)
    if errors:
        print("Validation Errors:")
        for error in errors:
            print("-", error)
        return

    collection = get_collection()
    insert_into_mongo(df, collection)

    print("Data processed and stored in MongoDB Atlas successfully.")

if __name__ == "__main__":
    main()
