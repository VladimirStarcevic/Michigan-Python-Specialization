def info(name: str, gender: str, age: int, bday_month: int, hometown: str) -> tuple[str, str, int, int, str]:
    return name, gender, age, bday_month, hometown


info_list = info("Vladimir", "M", 46, 4, "Belgrade")
print(info_list)


