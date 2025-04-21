from datetime import datetime

def write_readme():
    today = datetime.now().strftime("%Y-%m-%d")
    content = f"""# 📅 {today} 的小日记

今天是 {today}，今天又是美好的一天。
不管怎么样，每一天都是人生中不可复制的一天，就算做着重复的事，也是独一无二的。
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    write_readme()
