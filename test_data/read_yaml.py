import yaml

def get_yaml(key="liuxing"):
    with open("./test_data/data.yaml","r",encoding="utf-8") as data:
        # 读取出来是字符串
        d = data.read()

        zd = yaml.load(d)[key]
        print(zd)
        return zd

if __name__ == '__main__':
    get_yaml()