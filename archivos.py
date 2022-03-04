def read():
    numbers=[]
    with open("./archivos/numbers.txt", "r" ,encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names=["jairo","perez","cuestas","roc6o","maria"]
    with open("./archivos/names1.txt","a",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()

if __name__=="__main__":
    run()