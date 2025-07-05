import pandas as pd

def get_block_deals():
    data = [
        {"Stock": "HDFC Bank", "Type": "Block Deal", "Qty": "1M", "Price": "₹1680"},
        {"Stock": "Infosys", "Type": "Bulk Deal", "Qty": "2M", "Price": "₹1520"}
    ]
    return pd.DataFrame(data)
