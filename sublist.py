def sublist(sample):
    sample_len=len(sample)
    sublist=[]
    start=0
    end=3
    while end<=sample_len:
        sub=sample[start:end]
        sublist.append(sub)
        start=start+1
        end=start+3
    return sublist

def check_winner():
    win=False
    X_filled=[]
    O_filled=[]
    winning_list=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    X_filled=[0,1,2]
    O_filled=[0,3,6,1,4,7]
    sublist_x_filled= list(sublist(X_filled))
    sublist_o_filled= list(sublist(O_filled))
    print(type(sublist_x_filled),type(sublist_o_filled))
    for i in winning_list:
        for m in sublist_x_filled:
            l=sorted(m)
            if l==i:
                win=True
                break
        for m in sublist_o_filled:
            l=sorted(m)
            if l==i:
                win=True
                break
        return win
            
if __name__=="__main__":
    sample=[0,3,4,2,6]
    print(sublist(sample))
    print(check_winner())
    
            
            
        
    