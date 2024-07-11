import argparse
from warframe_items_client import WarframeItemsClient


def main():
    parser = argparse.ArgumentParser(description="CLI tool for Warframe Items Client")
    parser.add_argument("items", nargs="+", help="List of item URLs to query")
    args = parser.parse_args()

    warframe_items_client = WarframeItemsClient(args.items)
    warframe_items_client.get_excel()
    print("Excel file 'orders.xlsx' has been created with the item orders.")
