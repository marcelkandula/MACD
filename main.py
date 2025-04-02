import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

def ema(series, span):
    alpha = 2 / (span + 1)
    ema_values = [series[0]]
    for price in series[1:]:
        ema_values.append(alpha * price + (1 - alpha) * ema_values[-1])
    return np.array(ema_values)

def compute_macd_signal(prices):
    ema12 = ema(prices, 12)
    ema26 = ema(prices, 26)
    macd = ema12 - ema26
    signal = ema(macd, 9)
    return macd, signal

def get_buy_sell_signals(macd, signal):
    buy_signals, sell_signals = [], []
    for i in range(1, len(macd)):
        if macd[i-1] < signal[i-1] and macd[i] > signal[i]:
            buy_signals.append(i)
        elif macd[i-1] > signal[i-1] and macd[i] < signal[i]:
            sell_signals.append(i)
    return buy_signals, sell_signals


def simulate_trading(prices, buy_signals, sell_signals, dates):
    cash = 1000.0
    position = 0.0
    portfolio_value = []
    transactions = []
    buy_price = None
    profitable_trades = 0
    losing_trades = 0

    for i in range(len(prices)):
        if i in buy_signals and cash > 0:
            buy_price = prices[i]
            position = cash / buy_price
            cash = 0
            transactions.append(('BUY', dates[i], buy_price, None))

        elif i in sell_signals and position > 0:
            sell_price = prices[i]
            sell_date = dates[i]
            cash = position * sell_price
            profit_pct = (sell_price - buy_price) / buy_price * 100 if buy_price else 0
            position = 0

            if profit_pct > 0:
                profitable_trades += 1
            else:
                losing_trades += 1

            transactions.append(('SELL', sell_date, sell_price, profit_pct))
            buy_price = None

        portfolio_value.append(cash + position * prices[i])

    final_portfolio_value = cash + (position * prices[-1] if position > 0 else 0)
    return portfolio_value, transactions, final_portfolio_value, profitable_trades, losing_trades


def main():
    ticker = "MSFT"
    filename = "MSFT.csv"
    filename2 = "NVDA.csv"
    ticker2 = "NVDA"

    #df = yf.download(ticker2, period="3y")[['Close']].dropna()
    #df.to_csv(filename2, index=True)

    df = pd.read_csv(filename2, index_col=0, parse_dates=True)
    prices = df['Close'].astype(float).values
    dates = df.index

    macd, signal = compute_macd_signal(prices)

    buy_signals, sell_signals = get_buy_sell_signals(macd, signal)
    portfolio, transactions, final_value, profitable, losing = simulate_trading(prices, buy_signals, sell_signals, dates)

    print("\nTransakcje:")
    print("{:<10} {:<12} {:<15} {:<15}".format("Typ", "Data", "Cena", "Zysk/Strata (%)"))
    for trade in transactions:
        date_str = trade[1].strftime('%Y-%m-%d')
        profit_str = f"{trade[3]:.2f}%" if trade[3] is not None else "-"
        print("{:<10} {:<12} {:<15.2f} {:<15}".format(
            trade[0], date_str, trade[2], profit_str))

    print("\nPodsumowanie strategii:")
    print(f"Końcowa wartość portfela: {final_value:.2f} ")
    print(f"Początkowa inwestycja: 1000.00 ")
    print(f"Zysk/Strata całkowita: {(final_value - 1000):.2f}  ({(final_value / 1000 - 1) * 100:.2f}%)")
    print(f"Liczba zyskownych transakcji: {profitable}")
    print(f"Liczba stratnych transakcji: {losing}")
    print(f"Skuteczność strategii: {profitable / (profitable + losing) * 100:.2f}%" if (profitable + losing) > 0 else "Brak transakcji")

    plt.figure()
    plt.plot(df.index, prices, label='Cena zamknięcia')
    plt.title('Notowania ' + ticker2)
    plt.legend()
    plt.show()


    plt.figure()
    plt.plot(df.index, macd, label='MACD')
    plt.plot(df.index, signal, label='SIGNAL')
    plt.scatter(df.index[buy_signals], macd[buy_signals], color='green', marker='^', label='Kupno')
    plt.scatter(df.index[sell_signals], macd[sell_signals], color='red', marker='v', label='Sprzedaż')
    plt.title('MACD & SIGNAL')
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(df.index, portfolio, label='Wartość portfela')
    plt.title('Symulacja transakcji')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
