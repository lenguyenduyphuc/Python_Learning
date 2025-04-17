class Spree:
    # init budget
    budget = 0.0
    
    def __init__(self, store, amount):
        self.__store = store
        self.__amount = amount

    def getStores(self):
        return self.__store
    
    def getAmount(self):
        return self.__amount
    
    @classmethod
    def setBudget(self, bud):
        self.budget = bud

    def __str__(self):
        return f"Stores: {self.__store} Amount spend: {self.__amount:.2f}"

def main():
    max_budget = float(input("What is the amount you want to spend? $"))
    Spree.setBudget(max_budget)    

    num_stores = int(input("Enter the number of stores visited (where a purchase was made): "))
    purchase = []
    for _ in range(num_stores):
        print()
        store = input("Name of Store: ")
        amount = float(input("Amount spent in store: $"))
        purchase.append(Spree(store, amount))

    print()
    print(f"Your budget was: ${Spree.budget:.2f}")
    total_spent = 0
    for p in purchase:
        print(p)
        total_spent += p.getAmount()

    print(f"You spent ${total_spent:.2f}")

    if total_spent <= max_budget:
        print("Nice! You stayed within your budget.")
    else:
        over = total_spent - max_budget
        print(f"You went over budget by ${over:,.2f}.")

if __name__ == "__main__":
    main()

