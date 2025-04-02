# 📈 MACD Trading Strategy Simulation  

This project evaluates the **Moving Average Convergence Divergence (MACD)** indicator for stock trading. It downloads historical stock prices, computes MACD and signal lines, identifies buy/sell signals, and simulates trading to analyze profitability.  

## ✨ Features  
- **MACD Calculation**: Computes the MACD and signal line using Exponential Moving Averages (EMA).  
- **Buy/Sell Signals**: Identifies trading opportunities based on MACD crossovers.  
- **Trading Simulation**: Simulates a simple trading strategy with a $1000 initial investment.  
- **Performance Analysis**: Summarizes trading results, including final portfolio value and win/loss rate.  
- **Visualization**: Plots stock prices, MACD signals, and portfolio performance.  

## 📥 Installation  

Ensure you have Python and the required libraries installed:  

```bash
pip install numpy pandas yfinance matplotlib
```

## 🚀 Usage  

1. **Download Historical Data** (optional): Modify `ticker` and download data using `yfinance`.  
2. **Run the Script**:  

```bash
python macd_trading.py
```

3. **Interpret Results**: The script prints transaction details and performance metrics, and displays stock price, MACD, and portfolio charts.  

## 🛠 Code Breakdown  

- **`ema(series, span)`**: Computes the Exponential Moving Average.  
- **`compute_macd_signal(prices)`**: Calculates MACD and the signal line.  
- **`get_buy_sell_signals(macd, signal)`**: Identifies buy/sell points based on MACD crossovers.  
- **`simulate_trading(prices, buy_signals, sell_signals, dates)`**: Simulates trades and evaluates strategy performance.  
- **`main()`**: Orchestrates the process, including fetching data, computing indicators, simulating trades, and visualizing results.  

## 📊 Example Output  

```
Transakcje:
Typ        Data         Cena            Zysk/Strata (%)
BUY        2023-05-12   310.50          -
SELL       2023-06-15   325.75          4.92%
...

Podsumowanie strategii:
Końcowa wartość portfela: 1082.50  
Początkowa inwestycja: 1000.00  
Zysk/Strata całkowita: 82.50  (8.25%)  
Liczba zyskownych transakcji: 3  
Liczba stratnych transakcji: 1  
Skuteczność strategii: 75.00%  
```

## 📌 Notes  
- The strategy uses historical data for backtesting and **does not predict future prices**.  
- Modify the ticker symbol and data source for different stocks.  

## 📜 License  
This project is open-source under the **MIT License**.  

🚀 Happy Trading! 📈