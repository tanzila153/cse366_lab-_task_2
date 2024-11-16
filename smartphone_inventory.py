import matplotlib.pyplot as plt 

class TradingAgent:
    def __init__(self, avg_price, critical_stock=10, reorder_quantity=15, minimum_order=10):
        self.avg_price = avg_price  # Average price of the smartphone
        self.critical_stock = critical_stock  # Critical stock level threshold
        self.reorder_quantity = reorder_quantity  # Default order quantity
        self.minimum_order = minimum_order  # Minimum order if stock is critical

    def decide_order(self, current_price, stock_level):
        # Calculate the threshold price (20% below average price)
        discount_threshold = 0.8 * self.avg_price
        
        # Check if the price is below the threshold and stock is not critically low
        if current_price < discount_threshold and stock_level > self.critical_stock:
            return self.reorder_quantity  # Order standard amount if price is low
            
        # Check if stock is critically low
        elif stock_level < self.critical_stock:
            return self.minimum_order  # Order minimum quantity if stock is low
        
        # Otherwise, order not
        return 0

# Simulation parameters
average_price = 600  # Assume average price is 600 BDT
price_fluctuations = [640, 580, 570, 550, 600, 580, 550, 560, 530, 610, 620]  # Price data over time
stock_levels = [15, 16, 13, 9, 6, 17, 20, 30, 18, 10, 5]  # Stock data over time
order_history = []

# Create an instance of the agent
agent = TradingAgent(avg_price=average_price)

# Process each time step
for current_price, stock_level in zip(price_fluctuations, stock_levels):
    tobuy = agent.decide_order(current_price, stock_level)
    order_history.append(tobuy)
    print(f"Price: {current_price}, Stock: {stock_level}, Order: {tobuy} units")

# Plotting the results
plt.figure(figsize=(11, 5))
plt.plot(stock_levels, label='Stock Level', marker='o')
plt.plot(order_history, label='Orders Placed', marker='x')
plt.xlabel("Time Step")
plt.ylabel("Quantity")
plt.title("Smartphone Inventory and Order Placement Over Time")
plt.legend()
plt.grid(True)
plt.show()