def budget_manager(initial_budget):
    budget = initial_budget  

    def manager(action, amount = 0):
        nonlocal budget
        if action == "add":
            budget += amount
            print(f"income is {amount}. current buget is {budget}")
        elif action == "spend":
            if amount > budget:
                print(f"budget is not enough, your budget is {budget} you can not spend {amount}.")
            else:
                budget -= amount
                print(f"you spend {amount}, current budget is {budget}")
        elif action == "get":
            print(f"current budget is {budget}")
            return budget 
        else:
            print("action is invalid")
    return manager

my_budget = budget_manager(500)
my_budget("add" , 700)
my_budget("spend" , 200)
my_budget("get")
my_budget("spend" , 1500)
