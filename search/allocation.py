def calc_num_of_carriages(k, w_list, P):
    """一台あたりのトラックの積載量がPの時、
    荷物w_listのうちいくつ荷物を積めるかを返す"""
    num = 0  # 積み込んだ荷物
    for i in range(k):
        #  ループ数はトラックの数だけ
        total_weight_in_a_truck = 0  # 1台に積む荷物の重さの合計
        for w in w_list[num:]:
            if w > P:
                # 一つでも積めないものがあるとダメなのでその場合は0
                return 0
            total_weight_in_a_truck += w  # トラックに積んでみる
            if total_weight_in_a_truck > P:  # 積載量を超えたら
                break
            else:
                # 積むことができたら積める荷物の数を+1
                num += 1
    return num


def binary_search(k, w_list):
    """トラックの台数kと、荷物のそれぞれの重さを表すリストw_listを引数に取って、
    積載量をPとした時にトラックに積み込むことができる荷物の数をチェックするために二分探索を実施する"""
    left = 0
    right = 100000 * 10000  # 荷物の最大個数 * 荷物一つあたりの最大重量 = 全体の最大積載量
    while right - left > 1:
        mid = int((left + right) / 2)
        num_of_carriages = calc_num_of_carriages(k, w_list, mid)
        if len(w_list) <= num_of_carriages:
            """積載量をPとした時のトラックに積み込むことができる荷物の量がw_listの長さ以上の場合
            積載量Pでは多すぎるということなので、左半分を採用する"""
            right = mid
        elif len(w_list) > num_of_carriages:
            """積載量をPとした時のトラックに積み込むことができる荷物の量がw_listの長さより短い場合
            積載量Pでは足りないということなので、右半分を採用する"""
            left = mid
    """右端点を返す"""
    return right


# main
if __name__ == '__main__':
    nAndK = input().split(' ')
    n = int(nAndK[0])  # 荷物の個数
    k = int(nAndK[1])  # トラックの台数
    w_list = [int(input()) for i in range(n)]  # n個の荷物のそれぞれの重さ
    res = binary_search(k, w_list)
    print(res)
