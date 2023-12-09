#!/usr/bin/env python3
WARU = 10**9 + 7


def main():
    n = int(input())
    s = input()
    allow_char = "atcoder"
    allow_char_list = [char for char in s if char in allow_char]
    s = "".join(allow_char_list)
    cnt = 0

    a_index = [i for i, v in enumerate(s) if v == "a"]
    t_index = [i for i, v in enumerate(s) if v == "t"]
    c_index = [i for i, v in enumerate(s) if v == "c"]
    o_index = [i for i, v in enumerate(s) if v == "o"]
    d_index = [i for i, v in enumerate(s) if v == "d"]
    e_index = [i for i, v in enumerate(s) if v == "e"]
    r_index = [i for i, v in enumerate(s) if v == "r"]

    print(cnt % WARU)
    # あとで消す！！！
    print(f"s= {s}")


if __name__ == "__main__":
    main()
