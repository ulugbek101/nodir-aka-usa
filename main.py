import numpy as np
import matplotlib.pyplot as plt

# Create time ranges
t_years = np.linspace(0, 10, 100)  # for yearly data
t_days = np.linspace(0, 10, 100)   # for daily problems
t_months = np.linspace(0, 12, 100) # for gym problem

# Equations
startup_users = 1000 * 3**t_years
car_value = 25000 * 0.8**t_years
savings = 2000 * 1.05**t_years
town_population = 8000 * 1.06**t_years
donations = 100 * 2**(t_days-1)
downloads = 500 * 1.8**(t_days-1)
gym_members = 1200 * 0.9**(t_months)
investment = 5000 * 1.12**t_years
virus_spread = 5 * 3**(t_days/2)

# Plotting
plt.figure(figsize=(18, 12))

# 1. Startup Users
plt.subplot(3, 3, 1)
plt.plot(t_years, startup_users, label="Users", color="blue")
plt.title("Startup Users Growth")
plt.xlabel("Years")
plt.ylabel("Users")
plt.grid(True)

# 2. Car Value
plt.subplot(3, 3, 2)
plt.plot(t_years, car_value, label="Car Value", color="green")
plt.title("Car Depreciation")
plt.xlabel("Years")
plt.ylabel("Value ($)")
plt.grid(True)

# 3. Savings Growth
plt.subplot(3, 3, 3)
plt.plot(t_years, savings, label="Savings", color="purple")
plt.title("Jasmin's Savings")
plt.xlabel("Years")
plt.ylabel("Amount ($)")
plt.grid(True)

# 4. Town Population
plt.subplot(3, 3, 4)
plt.plot(t_years, town_population, label="Population", color="orange")
plt.title("Town Population Growth")
plt.xlabel("Years")
plt.ylabel("People")
plt.grid(True)

# 5. Charity Donations
plt.subplot(3, 3, 5)
plt.plot(t_days, donations, label="Donations", color="red")
plt.title("Charity Donations Growth")
plt.xlabel("Days")
plt.ylabel("Donations ($)")
plt.grid(True)

# 6. App Downloads
plt.subplot(3, 3, 6)
plt.plot(t_days, downloads, label="Downloads", color="cyan")
plt.title("App Downloads Growth")
plt.xlabel("Days")
plt.ylabel("Downloads")
plt.grid(True)

# 7. Gym Membership
plt.subplot(3, 3, 7)
plt.plot(t_months, gym_members, label="Members", color="brown")
plt.title("Gym Membership Decline")
plt.xlabel("Months")
plt.ylabel("Members")
plt.grid(True)

# 8. Investment Growth
plt.subplot(3, 3, 8)
plt.plot(t_years, investment, label="Investment", color="pink")
plt.axhline(y=10000, color='black', linestyle='--', label="Double Value")
plt.title("Investment Growth")
plt.xlabel("Years")
plt.ylabel("Value ($)")
plt.legend()
plt.grid(True)

# 9. Virus Spread
plt.subplot(3, 3, 9)
plt.plot(t_days, virus_spread, label="Infected", color="darkred")
plt.title("Virus Spread")
plt.xlabel("Days")
plt.ylabel("Infected People")
plt.grid(True)

plt.tight_layout()
plt.show()
