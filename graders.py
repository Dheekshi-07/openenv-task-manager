def grade_easy(score):
    return min(score, 1.0)

def grade_medium(score):
    return min(score * 0.8, 1.0)

def grade_hard(score):
    return min(score * 0.6, 1.0)


def run_all_graders(total_score):
    return {
        "easy": grade_easy(total_score),
        "medium": grade_medium(total_score),
        "hard": grade_hard(total_score),
    }