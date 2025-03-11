def shuffle_deck(N, shuffle_type):
    original_deck = list(range(N))
    current_deck = original_deck[:]
    def perform_shuffle(deck, shuffle_type):
        if shuffle_type == "out":
            mid = (N + 1) // 2
        else:
            mid = N // 2
        left_half = deck[:mid]
        right_half = deck[mid:]
        shuffled = []
        if shuffle_type == "out":
            for i in range(len(right_half)):
                shuffled.append(left_half[i])
                shuffled.append(right_half[i])
            if len(left_half) > len(right_half):
                shuffled.append(left_half[-1])
        else:
            for i in range(len(left_half)):
                shuffled.append(right_half[i])
                shuffled.append(left_half[i])
            if len(right_half) > len(left_half):
                shuffled.append(right_half[-1])
        return shuffled
    count = 0
    while True:
        current_deck = perform_shuffle(current_deck, shuffle_type)
        count += 1
        if current_deck == original_deck:
            return count
N, shuffle_type = input().split()
N = int(N)
print(shuffle_deck(N, shuffle_type))