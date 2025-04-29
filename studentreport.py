import random
import time

def get_scores(students):
    for student in students:
        for score in student['scores']:
            yield student['name'], score

def average(scores):
    if not scores:
        return 0
    if len(scores) == 1:
        return scores[0]
    return (scores[0] + (len(scores) - 1) * average(scores[1:])) / len(scores)

def log_and_retry(tries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(tries + 1):
                print(f"Calling {func.__name__} (attempt {attempt + 1})")
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}")
                    time.sleep(0.5)
            print(f"Failed after {tries + 1} tries.")
        return wrapper
    return decorator

@log_and_retry(3)
def generate_report(student):
    if random.random() < 0.3:
        raise Exception("Random failure.")
    avg_score = average(student['scores'])
    print(f"{student['name']}'s average score: {avg_score:.2f}")

students = [
    {"name": "Ayomide", "scores": [70, 80, 90]},
    {"name": "Rasheed", "scores": [60, 75, 85]},
]

print("Student Scores:")
for name, score in get_scores(students):
    print(f"{name}: {score}")

print("\nReports:")
for student in students:
    generate_report(student)
