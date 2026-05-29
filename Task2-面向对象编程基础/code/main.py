from member_manager import MemberManager

def print_menu():
    print("=" * 44)
    print("========== RoboMaster 队员积分管理系统 ==========")
    print("1. 添加队员")
    print("2. 查看所有队员")
    print("3. 为队员加分")
    print("4. 为队员扣分")
    print("5. 按积分排名")
    print("6. 删除队员")
    print("7. 退出系统")
    print("=" * 44)

def add_member(manager):
    print("\n----- 添加队员 -----")
    name = input("请输入队员姓名：").strip()
    if not name:
        print("❌ 姓名不能为空！")
        return
    
    valid_groups = ["视觉", "电控", "机械", "运营"]
    while True:
        group = input("请输入组别（视觉/电控/机械/运营）：").strip()
        if group in valid_groups:
            break
        print("❌ 无效组别，请输入视觉、电控、机械或运营！")
    
    member = manager.add_member(name, group)
    print(f"✅ 添加成功！队员编号：{member.member_id}，姓名：{member.name}，组别：{member.group}，初始积分：{member.score}")

def view_all_members(manager):
    print("\n----- 所有队员 -----")
    members = manager.get_all_members()
    if not members:
        print("暂无队员信息！")
        return
    
    print("{:<8} {:<8} {:<8} {:<8}".format("编号", "姓名", "组别", "积分"))
    print("-" * 32)
    for member in members:
        print("{:<8} {:<8} {:<8} {:<8}".format(member.member_id, member.name, member.group, member.score))
    print("-" * 32)

def add_points(manager):
    print("\n----- 为队员加分 -----")
    member_id = input("请输入队员编号：").strip()
    if not member_id.startswith("RM"):
        print("❌ 编号格式错误！应为 RM 开头，如 RM0001")
        return
    
    try:
        points = int(input("请输入要加的分数："))
    except ValueError:
        print("❌ 请输入有效的数字！")
        return
    
    member, error = manager.add_points(member_id, points)
    if error:
        print("❌ " + error)
    else:
        print(f"✅ 成功为 {member.name} 增加 {points} 分，当前积分：{member.score}")

def subtract_points(manager):
    print("\n----- 为队员扣分 -----")
    member_id = input("请输入队员编号：").strip()
    if not member_id.startswith("RM"):
        print("❌ 编号格式错误！应为 RM 开头，如 RM0001")
        return
    
    try:
        points = int(input("请输入要扣的分数："))
    except ValueError:
        print("❌ 请输入有效的数字！")
        return
    
    member, error = manager.subtract_points(member_id, points)
    if error:
        print("❌ " + error)
    else:
        print(f"✅ 成功为 {member.name} 扣除 {points} 分，当前积分：{member.score}")

def rank_members(manager):
    print("\n----- 积分排行榜 -----")
    members = manager.rank_members()
    if not members:
        print("暂无队员信息！")
        return
    
    print("{:<6} {:<8} {:<8} {:<8} {:<8}".format("排名", "编号", "姓名", "组别", "积分"))
    print("-" * 40)
    
    medals = ["🥇", "🥈", "🥉"]
    for i, member in enumerate(members, 1):
        medal = medals[i-1] if i <= 3 else "  "
        print("{}{:<4} {:<8} {:<8} {:<8} {:<8}".format(medal, i, member.member_id, member.name, member.group, member.score))
    
    print("-" * 40)

def delete_member(manager):
    print("\n----- 删除队员 -----")
    member_id = input("请输入要删除的队员编号：").strip()
    if not member_id.startswith("RM"):
        print("❌ 编号格式错误！应为 RM 开头，如 RM0001")
        return
    
    member = manager.find_member_by_id(member_id)
    if not member:
        print(f"❌ 未找到编号为 {member_id} 的队员！")
        return
    
    print(f"⚠ 即将删除队员：{member.member_id}\t{member.name}\t{member.group}\t{member.score}分")
    confirm = input("确认删除？(y/n)：").strip().lower()
    if confirm == "y":
        success, error = manager.delete_member(member_id)
        if success:
            print(f"✅ 队员 {member.member_id} {member.name} 已删除！")
        else:
            print("❌ " + error)
    else:
        print("取消删除操作")

def main():
    manager = MemberManager()
    
    while True:
        print_menu()
        
        try:
            choice = int(input("请选择操作（1-7）："))
        except ValueError:
            print("❌ 请输入有效的数字！")
            continue
        
        if choice == 1:
            add_member(manager)
        elif choice == 2:
            view_all_members(manager)
        elif choice == 3:
            add_points(manager)
        elif choice == 4:
            subtract_points(manager)
        elif choice == 5:
            rank_members(manager)
        elif choice == 6:
            delete_member(manager)
        elif choice == 7:
            print("\n👋 感谢使用 RoboMaster 队员积分管理系统，再见！")
            break
        else:
            print("❌ 无效选择，请输入 1-7 之间的数字！")
        
        if choice != 7:
            input("\n按回车键继续...")
            print()

if __name__ == "__main__":
    main()