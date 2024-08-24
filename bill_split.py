def calculate_balances(n, names, contributions):
    total_expense = sum(contributions)
    fair_share = total_expense / n

    # Calculate the balance for each person (positive means they should receive money, negative means they should pay money)
    balances = [(names[i], contributions[i] - fair_share) for i in range(n)]
    
    return balances

def settle_balances(balances):
    payers = []
    receivers = []

    # Separate payers and receivers
    for name, balance in balances:
        if balance < 0:
            payers.append((name, -balance))  # Store as positive for easier calculations
        elif balance > 0:
            receivers.append((name, balance))

    transactions = []

    # Settle the amounts
    while payers and receivers:
        payer_name, payer_amount = payers.pop(0)
        receiver_name, receiver_amount = receivers.pop(0)
        
        settled_amount = min(payer_amount, receiver_amount)
        
        transactions.append((payer_name, receiver_name, settled_amount))

        # Adjust the remaining amounts
        payer_amount -= settled_amount
        receiver_amount -= settled_amount

        if payer_amount > 0:
            payers.insert(0, (payer_name, payer_amount))
        if receiver_amount > 0:
            receivers.insert(0, (receiver_name, receiver_amount))

    return transactions

def main():
    # Input the number of people
    n = int(input("Enter the number of people: "))

    names = []
    contributions = []

    for i in range(n):
        name = input(f"Enter the name of person {i+1}: ")
        contribution = float(input(f"Enter the contribution of {name}: "))
        names.append(name)
        contributions.append(contribution)

    balances = calculate_balances(n, names, contributions)
    transactions = settle_balances(balances)

    # Output the results
    for payer, receiver, amount in transactions:
        print(f"{payer} must pay {receiver} an amount of {amount:.2f}")

if __name__ == "__main__":
    main()
