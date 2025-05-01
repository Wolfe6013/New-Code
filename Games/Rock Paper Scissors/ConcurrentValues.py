def FindReccursion(InnerList,FullList): #[var,var,...,next]
    ContainedList = InnerList
    Best: list = []
    CallList = FullList
    ContainedList.append("%@*&$ED*&DUAUO*UWQ#*#(**(@*#&$)!)!(#*&$&%*#&#^&^YFYSEUF&*46^#GF^36*)f7")
    for z in range(len(ContainedList)):
        for x in FullList:
            ConsecutiveCorrect = 0
            Now: list = []
            failed = False
            final = False
            started = False
            for y in range(len(ContainedList)):
                if CallList[y] == ContainedList[y] and not failed:
                    ConsecutiveCorrect += 1
                    Now.append(CallList[y])
                    started = True
                elif started and final == False:
                    Now.append(CallList[y])
                    final = True
                else:
                    failed = True
            if len(Now) > len(Best):
                Best = Now
            CallList.append(CallList[0])
            CallList.pop(0)
        ContainedList.append(ContainedList[0])
        ContainedList.pop(0)
    ContainedList.remove("%@*&$ED*&DUAUO*UWQ#*#(**(@*#&$)!)!(#*&$&%*#&#^&^YFYSEUF&*46^#GF^36*)f7")
    return Best

if __name__ == '__main__':
    List1 = [1,2,3,4,5,6,7,8,9]
    List2 = ["y",4,5,6,3,0,"f"]
    print(f"Final - {FindReccursion(List2,List1)}")