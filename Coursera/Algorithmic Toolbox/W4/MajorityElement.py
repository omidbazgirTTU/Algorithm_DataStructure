def find_majority(n, array):
    data_dic = {}
    thresh = int(n/2)
    for i in range(n):
        if array[i] in data_dic.keys():
            data_dic[array[i]] +=1
            if data_dic[array[i]] > thresh:
                return 1
        else:
            data_dic[array[i]] = 1
    return 0



if __name__ == "__main__":
    n_k = list(map(int,input().split()))[0]
    k = list(map(int, input().split()))
    print(find_majority(n_k, k))
