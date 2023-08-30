from app import db
from app.models import Stock, SCHEMA, environment
from sqlalchemy.sql import text

# Seed the database with 4 stocks


def seed_stocks():
    # Create watchlists

    stocks_data = [
        {"symbol": "TSLA", "org_name": "Tesla", "current_price": 256.90},
        {"symbol": "AAPL", "org_name": "Apple", "current_price": 187.65},
        {"symbol": "AMZN", "org_name": "Amazon.com", "current_price": 135.07},
        {"symbol": "MSFT", "org_name": "Microsoft Corp", "current_price": 328.79},
        {"symbol": "NVDA", "org_name": "NVIDIA Corp.", "current_price": 492.64},
        {"symbol": "GOOGL", "org_name": "Alphabet", "current_price": 135.88},
        {"symbol": "PEP", "org_name": "PepsiCo", "current_price": 181.08},
        {"symbol": "COST", "org_name": "Costco Wholesale Corp", "current_price": 542.26},
        {"symbol": "CMCSA", "org_name": "Comcast Corp", "current_price": 47.12},
        {"symbol": "ADBE", "org_name": "Adobe", "current_price": 545.36},
        {"symbol": "TXN", "org_name": "Texas Instruments", "current_price": 169.23},
        {"symbol": "AVGO", "org_name": "Broadcom", "current_price": 892.28},
        {"symbol": "HON", "org_name": "Honeywell International",
            "current_price": 188.56},
        {"symbol": "INTC", "org_name": "Intel Corp", "current_price": 34.53},
        {"symbol": "TMUS", "org_name": "T-Mobile US", "current_price": 137.39},
        {"symbol": "SBUX", "org_name": "Starbucks Corp.", "current_price": 99.24},
        {"symbol": "NFLX", "org_name": "Netflix", "current_price": 434.67},
        {"symbol": "QCOM", "org_name": "QUALCOMM", "current_price": 113.27},
        {"symbol": "AMD", "org_name": "Advanced Micro Devices", "current_price": 106.59},
        {"symbol": "CSCO", "org_name": "Cisco Systems", "current_price": 56.81},
        {"symbol": "INTU", "org_name": "Intuit", "current_price": 540.58},
        {"symbol": "AMGN", "org_name": "Amgen", "current_price": 257.88},
        {"symbol": "AMAT", "org_name": "Applied Materials", "current_price": 150.95},
        {"symbol": "GILD", "org_name": "Gilead Sciences", "current_price": 77.66},
        {"symbol": "MDLZ", "org_name": "Mondelez International", "current_price": 71.57},
        {"symbol": "ADI", "org_name": "Analog Devices", "current_price": 181.57},
        {"symbol": "ADP", "org_name": "Automatic Data Processing",
            "current_price": 254.93},
        {"symbol": "ISRG", "org_name": "Intuitive Surgical", "current_price": 318.58},
        {"symbol": "REGN", "org_name": "Regeneron Pharmaceuticals",
            "current_price": 834.95},
        {"symbol": "PYPL", "org_name": "PayPal Holdings", "current_price": 63.42},
        {"symbol": "VRTX", "org_name": "Vertex Pharmaceuticals",
            "current_price": 350.76},
        {"symbol": "FISV", "org_name": "Fiserv", "current_price": 112.00},
        {"symbol": "LRCX", "org_name": "Lam Research Corp", "current_price": 686.53},
        {"symbol": "ATVI", "org_name": "Activision Blizzard", "current_price": 91.98},
        {"symbol": "MU", "org_name": "Micron Technology", "current_price": 68.09},
        {"symbol": "MELI", "org_name": "MercadoLibre", "current_price": 1343.13},
        {"symbol": "CSX", "org_name": "CSX Corp", "current_price": 30.73},
        {"symbol": "PANW", "org_name": "Palo Alto Networks", "current_price": 237.90},
        {"symbol": "MRNA", "org_name": "Moderna", "current_price": 116.62},
        {"symbol": "SNPS", "org_name": "Synopsys", "current_price": 457.28},
        {"symbol": "ASML", "org_name": "ASML Holding NV", "current_price": 610.70},
        {"symbol": "CDNS", "org_name": "Cadence Design Systems",
            "current_price": 239.88},
        {"symbol": "CHTR", "org_name": "Charter Communications",
            "current_price": 439.51},
        {"symbol": "KLAC", "org_name": "KLA Corp", "current_price": 498.30},
        {"symbol": "ORLY", "org_name": "O'Reilly Automotive", "current_price": 952.15},
        {"symbol": "FTNT", "org_name": "Fortinet", "current_price": 61.22},
        {"symbol": "KDP", "org_name": "Keurig Dr Pepper", "current_price": 33.77},
        {"symbol": "MAR", "org_name": "Marriott International MD",
            "current_price": 205.35},
        {"symbol": "ABNB", "org_name": "Airbnb", "current_price": 130.61},
        {"symbol": "KHC", "org_name": "Kraft Heinz Co/The", "current_price": 33.67},
        {"symbol": "AEP", "org_name": "American Electric Power Co",
            "current_price": 79.44},
        {"symbol": "NXPI", "org_name": "NXP Semiconductors NV", "current_price": 205.88},
        {"symbol": "DXCM", "org_name": "Dexcom", "current_price": 103.42},
        {"symbol": "CTAS", "org_name": "Cintas Corp", "current_price": 505.99},
        {"symbol": "ADSK", "org_name": "Autodesk", "current_price": 221.55},
        {"symbol": "PDD", "org_name": "PDD Holdings ADR", "current_price": 98.14},
        {"symbol": "MCHP", "org_name": "Microchip Technology", "current_price": 81.99},
        {"symbol": "AZN", "org_name": "AstraZeneca PLC ADR", "current_price": 68.86},
        {"symbol": "IDXX", "org_name": "IDEXX Laboratories", "current_price": 510.81},
        {"symbol": "EXC", "org_name": "Exelon Corp", "current_price": 40.42},
        {"symbol": "PAYX", "org_name": "Paychex", "current_price": 122.53},
        {"symbol": "BIIB", "org_name": "Biogen", "current_price": 267.18},
        {"symbol": "LULU", "org_name": "Lululemon Athletica", "current_price": 376.73},
        {"symbol": "WDAY", "org_name": "Workday", "current_price": 243.14},
        {"symbol": "SGEN", "org_name": "Seagen", "current_price": 206.85},
        {"symbol": "PCAR", "org_name": "PACCAR", "current_price": 82.72},
        {"symbol": "GFS", "org_name": "GLOBALFOUNDRIES", "current_price": 54.69},
        {"symbol": "ODFL", "org_name": "Old Dominion Freight Line",
            "current_price": 430.31},
        {"symbol": "XEL",  "org_name": "Xcel Energy", "current_price": 57.68},
        {"symbol": "MRVL", "org_name": "Marvell Technology", "current_price": 57.34},
        {"symbol": "WBD", "org_name": "Warner Bros Discovery", "current_price": 13.11},
        {"symbol": "CPRT", "org_name": "Copart", "current_price": 45.07},
        {"symbol": "ROST", "org_name": "Ross Stores", "current_price": 121.65},
        {"symbol": "ILMN", "org_name": "Illumina", "current_price": 166.06},
        {"symbol": "EA", "org_name": "Electronic Arts", "current_price": 120.55},
        {"symbol": "DLTR", "org_name": "Dollar Tree", "current_price": 124.49},
        {"symbol": "CTSH", "org_name": "Cognizant Technology Solutions Corp",
            "current_price": 71.49},
        {"symbol": "FAST", "org_name": "Fastenal Co", "current_price": 57.78},
        {"symbol": "CRWD", "org_name": "Crowdstrike Holdings", "current_price": 149.18},
        {"symbol": "VRSK", "org_name": "Verisk Analytics", "current_price": 241.67},
        {"symbol": "WBA", "org_name": "Walgreens Boots Alliance", "current_price": 25.60},
        {"symbol": "CSGP", "org_name": "CoStar Group", "current_price": 82.60},
        {"symbol": "ANSS", "org_name": "ANSYS", "current_price": 315.96},
        {"symbol": "BKR", "org_name": "Baker Hughes Co", "current_price": 36.05},
        {"symbol": "MNST", "org_name": "Monster Beverage Corp", "current_price": 58.15},
        {"symbol": "ENPH", "org_name": "Enphase Energy", "current_price": 128.11},
        {"symbol": "CEG", "org_name": "Constellation Energy Corp",
            "current_price": 105.74},
        {"symbol": "FANG", "org_name": "Diamondback Energy", "current_price": 151.31},
        {"symbol": "ALGN", "org_name": "Align Technology", "current_price": 370.86},
        {"symbol": "TEAM", "org_name": "Atlassian Corp", "current_price": 202.26},
        {"symbol": "EBAY", "org_name":  "eBay", "current_price": 44.75},
        {"symbol": "DDOG", "org_name": "Datadog", "current_price": 94.16},
        {"symbol": "JD", "org_name": "JD.com  ADR", "current_price": 131.80},
        {"symbol": "ZM", "org_name": "Zoom Video Communications", "current_price": 68.67},
        {"symbol": "ZS", "org_name": "Zscaler", "current_price": 147.28},
        {"symbol": "LCID", "org_name": "Lucid Group", "current_price": 6.36},
        {"symbol": "SIRI", "org_name": "Sirius XM Holdings", "current_price": 4.58},
        {"symbol": "RIVN", "org_name": "Rivian Automotive", "current_price": 22.88}
    ]

    stocks_data2 = []

    for stock in stocks_data:
        value = Stock(symbol=stock['symbol'], org_name=stock['org_name'],
                      current_price=stock['current_price'])
        stocks_data2.append(value)

    # Add the watchlists to the database
    db.session.add_all(stocks_data2)
    db.session.commit()


def undo_stocks():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.stocks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM stocks"))

    db.session.commit()
