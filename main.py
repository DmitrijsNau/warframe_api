import argparse
import sys
from warframe_items_client import WarframeItemsClient


def main():
    parser = argparse.ArgumentParser(description="CLI tool for Warframe Items Client")
    parser.add_argument("items", nargs="*", help="List of item URLs to query")
    parser.add_argument("--interactive", "-i", action="store_true", help="Run in interactive mode to input item URLs")
    args = parser.parse_args()

    items = args.items

    if args.interactive or not items:
        print("Enter item URLs (type 'done' when finished):")
        while True:
            item_url = input("Item URL: ").strip()
            if item_url.lower() == "done":
                break
            items.append(item_url)

    if not items:
        print("No item URLs provided. Exiting.")
        return

    warframe_items_client = WarframeItemsClient(items)
    err = warframe_items_client.get_excel()
    if not err:
        print("Excel file 'orders.xlsx' has been created with the item orders.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
