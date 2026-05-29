class Member:
    next_id = 1

    def __init__(self, name, group):
        self.member_id = f"RM{Member.next_id:04d}"
        Member.next_id += 1
        self.name = name
        self.group = group
        self.score = 0

    def add_score(self, points):
        self.score += points

    def subtract_score(self, points):
        if points <= self.score:
            self.score -= points
            return True
        return False

    def __str__(self):
        return f"{self.member_id}\t{self.name}\t{self.group}\t{self.score}分"