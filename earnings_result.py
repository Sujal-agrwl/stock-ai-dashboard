import pandas as pd

def get_results_data():
    data = [
        {"Company": "TCS", "Quarter": "Q1 FY25", "Revenue": "₹58,000 Cr", "Profit": "₹11,000 Cr"},
        {"Company": "Infosys", "Quarter": "Q1 FY25", "Revenue": "₹37,000 Cr", "Profit": "₹6,800 Cr"}
    ]
    return pd.DataFrame(data)
