def calculate_love_score(name1, name2):
    # your code here
    combined_names = (name1 + name2).lower()

    true_count = 0
    love_count = 0

    for i in combined_names:
        if i in 'true':
            true_count += 1
        if i in 'love':
            love_count += 1

    total = str(true_count) + str(love_count)
    print(total)


# Call your function with hard coded values
calculate_love_score("Kanye West", "Kim Kardashian")