def fibonacci(n):
    a, b = 0, 1
    step_count = 0
    print("Fibonacci Series:", end=" ")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
        step_count += 1
    print("\nStep Count:", step_count)

n = int(input("Enter number of terms: "))
fibonacci(n)