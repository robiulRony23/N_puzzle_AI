import matplotlib.pyplot as plt

def offLine():
    data = [[] for j in range(0,10)]

    file = open("offLineFile.txt","r")
    while True:
        arr =[]
        f= file.readline();
        if len(f)==0:
            break
        if len(f)!=1:
            tmp= [i for i in f.split()]

            arr.append(int(tmp[1]))
            arr.append(int(tmp[2]))
            arr.append(float(tmp[3]))
            data[int(tmp[0])]+=[arr]

    file.close()

    for chk in range(1,4):
        for i in range(1,7):
            x1=[]
            y1=[]
            for j in range(0,len(data[i])):
                x1.append(data[1][j][0])
                y1.append(data[i][j][chk-1])
            # print("x",i,x1)
            # print("y",i,y1)
            if i==1:
                plt.plot(x1, y1, label="BFS")
            elif i==2:
                plt.plot(x1, y1, label="UCS")
            elif i==3:
                plt.plot(x1, y1, label="DLS")
            elif i==4:
                plt.plot(x1, y1, label="IDS")
            elif i==5:
                plt.plot(x1, y1, label="GBFS")
            elif i==6:
                plt.plot(x1, y1, label="A*")
        if chk==1:
            plt.xlabel('Distance(initial - goal state)')
            plt.ylabel('Estimated Cost')
            plt.title('Cost of algorithm')
        elif chk==2:
            plt.xlabel('Distance(initial - goal state)')
            plt.ylabel('Clock Time')
            plt.title('Clock Time of algorithms')
        elif chk==3:
            plt.xlabel('Distance(initial - goal state)')
            plt.ylabel('Node Crated')
            plt.title('Node created of algorithms')
        plt.legend()
        plt.show()