from typing import List


class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments: List[str] = []
        self.completed = False

    def change_name(self, new_name) -> str:
        if self.name != new_name:
            self.name = new_name
            return new_name
        return "Name cannot be the same."

    def change_due_date(self, new_date: str) -> str:
        if self.due_date != new_date:
            self.due_date = new_date
            return new_date
        return "Date cannot be the same."

    def add_comment(self, new_comment: str) -> None:
        self.comments.append(new_comment)

    def edit_comment(self, comment_number: int, new_comment:str) -> str or List[str]:
        if comment_number in range(len(self.comments)):
            self.comments[comment_number] = new_comment
            return ", ".join(c for c in self.comments)
        return "Cannot find comment."

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"