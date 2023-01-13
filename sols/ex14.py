MENU = {
    "sandwich": 10,
    "tea": 7,
    "seltzer": 4
}

CREDENTIAL_STORE = {
    "andrei": "016c756f0e615ef70ca05eb499a74d31c2ddec7244760d59d792583c0410b36d",
    "beano": "ece8ad1a81f33202c704bed53924089c39705c8cc06ce1ffdef895e408ae4eeb"
}


def restaurant() -> None:
    total = 0
    while order := input("Order: "):
        if order.strip() in MENU:
            total += MENU[order]
            print(f"{order} costs {MENU[order]}, total is {total}")
        else:
            print(f"We're out of {order}, sorry!")

    print(f"Your total is: {total}")


def login() -> None:
    from hashlib import sha256
    from getpass import getpass
    user = input("Username: ")
    if user not in CREDENTIAL_STORE:
        print("User not recognised!")
        return
    for i in range(3):
        pwd = getpass("Password: ")
        if sha256(bytes(pwd, encoding="utf-8")).hexdigest() == CREDENTIAL_STORE[user]:
            print("Sucessful login!")
            return
        else:
            print(f"Password incorrect! {3-i-1} tries remaining.")
    print("Login unsuccessful... Try again later.")
