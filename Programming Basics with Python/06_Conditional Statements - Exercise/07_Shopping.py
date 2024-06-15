GPU_PRICE = 250.00

budget = float(input())
gpu_amount = int(input())
cpu_amount = int(input())
ram_amount = int(input())

CPU_PRICE = GPU_PRICE * gpu_amount * 0.35
RAM_PRICE = GPU_PRICE * gpu_amount * 0.1

gpu_price = GPU_PRICE * gpu_amount
cpu_price = CPU_PRICE * cpu_amount
ram_price = RAM_PRICE * ram_amount

total_price = gpu_price + cpu_price + ram_price

if gpu_amount > cpu_amount:
    total_price = total_price * 0.85

if total_price <= budget:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
