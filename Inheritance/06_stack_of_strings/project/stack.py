from typing import List


class Stack:
    def __init__(self) -> None:
        self.data: List[str] = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        el = self.data.pop()
        return el

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return not self.data

    def __str__(self) -> str:
        reversed_data = reversed(self.data)
        res = f"[{', '.join(reversed_data)}]"
        return res


s = Stack()

s.push("1")
s.push("2")
s.push("3")
s.push("4")

print(s)
print(s.is_empty())
print(s.top())
print(s)

