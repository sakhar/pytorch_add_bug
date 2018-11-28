## prints different values for [-4] with ''add_()''
print('using add_():')
for i in range(10):
    values = pickle.load(open('values-np.p','rb'))
    x = torch.from_numpy(values[0])
    y = torch.from_numpy(values[1])
    print(x.add_(-0.7,y).data.detach().numpy()[-4:])

## always prints the same values for [-4] with ''add()''
print('using add():')
for i in range(10):
    values = pickle.load(open('values-np.p','rb'))
    x = torch.from_numpy(values[0])
    y = torch.from_numpy(values[1])
    print(x.add(-0.7,y).data.detach().numpy()[-4:])
