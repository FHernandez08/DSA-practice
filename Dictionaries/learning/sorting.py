scores = {
    'John': 90,
    'Alice': 95,
    'Bob': 88
}

sorted_by_keys = {k: scores[k] for k in sorted(scores)}
print(sorted_by_keys)

sorted_by_values = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1])}
print(sorted_by_values)