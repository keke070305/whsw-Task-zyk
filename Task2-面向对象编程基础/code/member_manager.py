from member import Member

class MemberManager:
    def __init__(self):
        self.members = []

    def add_member(self, name, group):
        member = Member(name, group)
        self.members.append(member)
        return member

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def get_all_members(self):
        return self.members

    def add_points(self, member_id, points):
        member = self.find_member_by_id(member_id)
        if not member:
            return None, "未找到编号为 {} 的队员！".format(member_id)
        if points <= 0:
            return None, "分数必须为正数！"
        member.add_score(points)
        return member, None

    def subtract_points(self, member_id, points):
        member = self.find_member_by_id(member_id)
        if not member:
            return None, "未找到编号为 {} 的队员！".format(member_id)
        if points <= 0:
            return None, "分数必须为正数！"
        if points > member.score:
            return None, "扣除分数不能大于当前积分（当前积分：{}）！".format(member.score)
        member.subtract_score(points)
        return member, None

    def rank_members(self):
        sorted_members = sorted(self.members, key=lambda x: x.score, reverse=True)
        return sorted_members

    def delete_member(self, member_id):
        member = self.find_member_by_id(member_id)
        if not member:
            return False, "未找到编号为 {} 的队员！".format(member_id)
        self.members.remove(member)
        return True, None

    def get_member_count(self):
        return len(self.members)