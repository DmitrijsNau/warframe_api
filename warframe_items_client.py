import requests
import pandas as pd


class WarframeItemsClient:
    def __init__(self, items_required_urls=[]):
        self.api_version = "v1"
        self.api_items_url = f"https://api.warframe.market/{self.api_version}/items/"
        self.items_required_urls = items_required_urls

    def get_items(self):
        all_items = []
        for item_url in self.items_required_urls:
            collection = []
            response = requests.get(f"{self.api_items_url}/{item_url}/orders")
            data = response.json()
            if not data.get("payload"):
                print(f"Item '{item_url}' not found.")
                continue
            # structure of data: {"payload": {"orders": []}}
            orders = data["payload"]["orders"]
            for order in orders:
                # only wants online users selling with mod rank 5
                if order["order_type"] == "sell" and order["user"]["status"] == "ingame" and order["mod_rank"] == 5:
                    collection.append(order)
            if collection:
                items_df = pd.DataFrame.from_records(collection)
                stats = items_df.describe()["platinum"][["min", "25%"]]
                item_stats = {"itemname": item_url, "min": stats["min"], "25%": stats["25%"]}
                all_items.append(item_stats)
        final_df = pd.DataFrame(all_items)
        return final_df

    def get_excel(self):
        items_df = self.get_items()
        if items_df.empty:
            print("No items found.")
            return 1
        items_df.to_excel("orders.xlsx", index=False)
        return 0
