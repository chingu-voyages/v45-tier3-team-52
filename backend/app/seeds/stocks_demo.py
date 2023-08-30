from app import db
from app.models import Stock, SCHEMA, environment
from sqlalchemy.sql import text

# Seed the database with 4 stocks


def seed_stocks():
    # Create watchlists

    stocks_data = [
        {"symbol": "TSLA", "org_name": "Tesla"},
        {"symbol": "AAPL", "org_name": "Apple"},
        {"symbol": "AMZN", "org_name": "Amazon.com"},
        {"symbol": "MSFT", "org_name": "Microsoft Corp"},
        {"symbol": "NVDA", "org_name": "NVIDIA Corp."},
        {"symbol": "GOOGL", "org_name": "Alphabet"},
        {"symbol": "PEP", "org_name": "PepsiCo"},
        {"symbol": "COST", "org_name": "Costco Wholesale Corp"},
        {"symbol": "CMCSA", "org_name": "Comcast Corp"},
        {"symbol": "ADBE", "org_name": "Adobe"},
        {"symbol": "TXN", "org_name": "Texas Instruments"},
        {"symbol": "AVGO", "org_name": "Broadcom"},
        {"symbol": "HON", "org_name": "Honeywell International"},
        {"symbol": "INTC", "org_name": "Intel Corp"},
        {"symbol": "TMUS", "org_name": "T-Mobile US"},
        {"symbol": "SBUX", "org_name": "Starbucks Corp."},
        {"symbol": "NFLX", "org_name": "Netflix"},
        {"symbol": "QCOM", "org_name": "QUALCOMM"},
        {"symbol": "AMD", "org_name": "Advanced Micro Devices"},
        {"symbol": "CSCO", "org_name": "Cisco Systems"},
        {"symbol": "INTU", "org_name": "Intuit"},
        {"symbol": "AMGN", "org_name": "Amgen"},
        {"symbol": "AMAT", "org_name": "Applied Materials"},
        {"symbol": "GILD", "org_name": "Gilead Sciences"},
        {"symbol": "MDLZ", "org_name": "Mondelez International"},
        {"symbol": "ADI", "org_name": "Analog Devices"},
        {"symbol": "ADP", "org_name": "Automatic Data Processing"},
        {"symbol": "ISRG", "org_name": "Intuitive Surgical"},
        {"symbol": "REGN", "org_name": "Regeneron Pharmaceuticals"},
        {"symbol": "PYPL", "org_name": "PayPal Holdings"},
        {"symbol": "VRTX", "org_name": "Vertex Pharmaceuticals "},
        {"symbol": "FISV", "org_name": "Fiserv"},
        {"symbol": "LRCX", "org_name": "Lam Research Corp"},
        {"symbol": "ATVI", "org_name": "Activision Blizzard"},
        {"symbol": "MU", "org_name": "Micron Technology"},
        {"symbol": "MELI", "org_name": "MercadoLibre"},
        {"symbol": "CSX", "org_name": "CSX Corp"},
        {"symbol": "PANW", "org_name": "Palo Alto Networks"},
        {"symbol": "MRNA", "org_name": "Moderna "},
        {"symbol": "SNPS", "org_name": "Synopsys "},
        {"symbol": "ASML", "org_name": "ASML Holding NV"},
        {"symbol": "CDNS", "org_name": "Cadence Design Systems"},
        {"symbol": "CHTR", "org_name": "Charter Communications"},
        {"symbol": "KLAC", "org_name": "KLA Corp"},
        {"symbol": "ORLY", "org_name": "O'Reilly Automotive"},
        {"symbol": "FTNT", "org_name": "Fortinet"},
        {"symbol": "KDP", "org_name": "Keurig Dr Pepper"},
        {"symbol": "MAR", "org_name": "Marriott International MD"},
        {"symbol": "ABNB", "org_name": "Airbnb "},
        {"symbol": "KHC", "org_name": "Kraft Heinz Co/The"},
        {"symbol": "AEP", "org_name": "American Electric Power Co"},
        {"symbol": "NXPI", "org_name": "NXP Semiconductors NV"},
        {"symbol": "DXCM", "org_name": "Dexcom"},
        {"symbol": "CTAS", "org_name": "Cintas Corp"},
        {"symbol": "ADSK", "org_name": "Autodesk"},
        {"symbol": "PDD", "org_name": "PDD Holdings ADR"},
        {"symbol": "MCHP", "org_name": "Microchip Technology"},
        {"symbol": "AZN", "org_name": "AstraZeneca PLC ADR"},
        {"symbol": "IDXX", "org_name": "IDEXX Laboratories"},
        {"symbol": "EXC", "org_name": "Exelon Corp"},
        {"symbol": "PAYX", "org_name": "Paychex"},
        {"symbol": "BIIB", "org_name": "Biogen"},
        {"symbol": "LULU", "org_name": "Lululemon Athletica"},
        {"symbol": "WDAY", "org_name": "Workday"},
        {"symbol": "SGEN", "org_name": "Seagen"},
        {"symbol": "PCAR", "org_name": "PACCAR"},
        {"symbol": "GFS", "org_name": "GLOBALFOUNDRIES"},
        {"symbol": "ODFL", "org_name": "Old Dominion Freight Line"},
        {"symbol": "XEL",  "org_name": "Xcel Energy"},
        {"symbol": "MRVL", "org_name": "Marvell Technology"},
        {"symbol": "WBD", "org_name": "Warner Bros Discovery"},
        {"symbol": "CPRT", "org_name": "Copart"},
        {"symbol": "ROST", "org_name": "Ross Stores"},
        {"symbol": "ILMN", "org_name": "Illumina"},
        {"symbol": "EA", "org_name": "Electronic Arts"},
        {"symbol": "DLTR", "org_name": "Dollar Tree"},
        {"symbol": "CTSH", "org_name": "Cognizant Technology Solutions Corp"},
        {"symbol": "FAST", "org_name": "Fastenal Co"},
        {"symbol": "CRWD", "org_name": "Crowdstrike Holdings"},
        {"symbol": "VRSK", "org_name": "Verisk Analytics"},
        {"symbol": "WBA", "org_name": "Walgreens Boots Alliance"},
        {"symbol": "CSGP", "org_name": "CoStar Group"},
        {"symbol": "ANSS", "org_name": "ANSYS"},
        {"symbol": "BKR", "org_name": "Baker Hughes Co"},
        {"symbol": "MNST", "org_name": "Monster Beverage Corp"},
        {"symbol": "ENPH", "org_name": "Enphase Energy"},
        {"symbol": "CEG", "org_name": "Constellation Energy Corp"},
        {"symbol": "FANG", "org_name": "Diamondback Energy"},
        {"symbol": "ALGN", "org_name": "Align Technology"},
        {"symbol": "TEAM", "org_name": "Atlassian Corp"},
        {"symbol": "EBAY", "org_name":  "eBay"},
        {"symbol": "DDOG", "org_name": "Datadog"},
        {"symbol": "JD", "org_name": "JD.com  ADR"},
        {"symbol": "ZM", "org_name": "Zoom Video Communications"},
        {"symbol": "ZS", "org_name": "Zscaler"},
        {"symbol": "LCID", "org_name": "Lucid Group"},
        {"symbol": "SIRI", "org_name": "Sirius XM Holdings"},
        {"symbol": "RIVN", "org_name": "Rivian Automotive"}
    ]

    stocks_data2 = []

    for stock in stocks_data:
        value = Stock(symbol=stock['symbol'], org_name=stock['org_name'])
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
