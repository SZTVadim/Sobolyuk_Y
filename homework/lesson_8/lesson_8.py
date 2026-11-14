# ЗАДАНИЕ 1: Распаковка списка и слияние
statuses = ["queued", "running", "testing", "deploy", "done"]
first, *middle, last = statuses
updated_statuses = [*middle, "failed", "skipped"]
print(first)
print(last)
print(updated_statuses)


# ЗАДАНИЕ 2: Словарь, слияние и вызов функции
def start_session(browser, timeout, headless):
    return f"{browser}, timeout={timeout}, headless={headless}"


browser = {"browser": "chrome", "timeout": 3000}
options = {"headless": True, "timeout": 5000}
config = {**browser, **options}
result = start_session(**config)
print(f"config: {config}\nresult: {result}")
