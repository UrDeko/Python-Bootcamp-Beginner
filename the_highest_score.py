def highest_score(scores):
    result = 0

    for score in scores:
        if score > result:
            result = score

    return result

if __name__ == "__main__":
    print(highest_score([180, 124, 165, 173, 189, 169, 146]))